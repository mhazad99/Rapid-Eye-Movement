"""
© 2021 CÉAMS. All right reserved.
See the file LICENCE for full license details.
"""
"""
    NonValidEventStep
    Step in the spindle detection interface to exclude non valid events for the spindle detection.
    Doc to open and read to understand : 
    Model and item : QAbstractItemModel -> QStandardItemModel -> QStandardItem
    View : QAbstractItemView -> QTreeView
"""
from RapidEyeMovementTools.RapidEyeMovCorrector.InputFileStep.InputFileStep import InputFileStep
from RapidEyeMovementTools.RapidEyeMovCorrector.NonValidEventStep.Ui_NonValidEventStep import Ui_NonValidEventStep
from RapidEyeMovementTools.RapidEyeMovCorrector.NonValidEventStep.EventsProxyModel import EventsProxyModel
from commons.NodeRuntimeException import NodeRuntimeException
from commons.BaseStepView import BaseStepView
from flowpipe.ActivationState import ActivationState

from widgets.TableDialog import TableDialog

import ast
import numpy as np
import pandas as pd
from qtpy import QtWidgets, QtCore
from qtpy.QtCore import Qt

class NonValidEventStep( BaseStepView,  Ui_NonValidEventStep, QtWidgets.QWidget):

    #node_id_ResetSignalArtefact_0 = "97edecf3-ab9b-4e8e-8759-2f117ac54221" # to activate if the signal during artifact are reset
    node_id_Dictionary_group = "98aaf913-882a-4728-a790-3852326874d6" # select the list of group for the current filename
    node_id_Dictionary_name = "e42725e7-1276-49f7-af92-d3efb2673e4e" # select the list of name for the current filename
    
    """
        NonValidEventStep
        Class to send messages between step-by-step interface and plugins.
        The goal is to inform "Reset Signal Interface" and "Discard Events" modules.
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # init UI
        self.setupUi(self)

        # Define modules and nodes to talk to
        #self._node_id_ResetSignalArtefact_0 = self.node_id_ResetSignalArtefact_0 # to activate if the signal during artifact are reset
        self._node_id_Dictionary_group = self.node_id_Dictionary_group # select the list of group for the current filename
        self._node_id_Dictionary_name = self.node_id_Dictionary_name # select the list of name for the current filename

        # Subscribe to context manager for each node you want to talk to
        self._artefact_group_topic = f'{self._node_id_Dictionary_group}.dictionary'
        self._pub_sub_manager.subscribe(self, self._artefact_group_topic)
        self._artefact_name_topic = f'{self._node_id_Dictionary_name}.dictionary'
        self._pub_sub_manager.subscribe(self, self._artefact_name_topic)
        # Dict to keep track of selected events
        self.group_dict = {} # the key is the filename and the item a string of groups
        self.name_dict = {}  # the key is the filename and the item a string of names
        self.files_check_event_model = None

        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[InputFileStep.context_files_view]
        # Extract the model (where the file information is stored) 
        #   To be aware of any change from the InputFiles Step
        self.files_model = self.reader_settings_view.files_model

    
    def init_models(self):
        # Access to the PsgReaderSettingsView to access easily informations about the files
        self.reader_settings_view = self._context_manager[InputFileStep.context_files_view]
        # Extract the model (where the file information is stored) 
        #   To be aware of any change from the InputFiles Step
        self.files_model = self.reader_settings_view.files_model
        # Create the model for the checkable events tree, based on self.files_model
        self.files_check_event_model = self.update_checkable_model(self.files_check_event_model)
        # The model for the list of files is from the PsgReaderSettingsView
        self.file_listview.setModel(self.files_model)
        # Add a proxy model to filter events
        self.event_proxy_model = EventsProxyModel(self)
        self.event_proxy_model.setSourceModel(self.files_check_event_model)
        self.event_proxy_model.setFilterKeyColumn(0) # col0: label, col1:count
        self.event_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.event_proxy_model.setRecursiveFilteringEnabled(False)
        # The model for the events checkable is created locally
        self.event_treeview.setModel(self.event_proxy_model)
        # Select/show the first file if any
        if self.files_check_event_model.rowCount()>0:
            filename = self.reader_settings_view.get_files_list(self.files_model)[0]
            self.file_listview.setCurrentIndex(self.reader_settings_view.get_file_index(filename,self.files_model))
            #self.on_file_selected()
            checkable_index = self.reader_settings_view.get_file_index(filename,self.files_check_event_model)
            # Map the index for the proxy model
            proxy_index = self.event_proxy_model.mapFromSource(checkable_index)
            self.event_treeview.setRootIndex(proxy_index)
        self.event_treeview.resizeColumnToContents(0)


    def load_settings(self):
        # Ask for the settings to the publisher to display on the SettingsView
        self._pub_sub_manager.publish(self, self._artefact_group_topic, 'ping')
        self._pub_sub_manager.publish(self, self._artefact_name_topic, 'ping')
        #self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_0+".get_activation_state", None)
        # Init the models and load the context manager
        self.init_models()
        # connect the checkbox state to the item selection
        self.files_check_event_model.itemChanged.connect(self.on_item_changed)


    def on_topic_update(self, topic, message, sender):
        """ Called by the publisher to init settings in the SettingsView 
            at any update, does not necessary answer to a ping.
            To listen to any modification not only when you ask (ping)
        """
        if topic==self._context_manager.topic:
            if message==InputFileStep.context_files_view: # key of the context dict
                self.init_models()
                # Update the model for the file list
                self.reader_settings_view = self._context_manager[InputFileStep.context_files_view]
                self.files_model = self.reader_settings_view.files_model
                # Saved selected states from self.files_check_event_model and the updated files list from self.files_model
                self.group_dict, self.name_dict = self._store_event_dict()
                # Create the model for the checkable events tree
                #   Select the events if available
                self.files_check_event_model = self.update_checkable_model(self.files_check_event_model)


    def on_topic_response(self, topic, message, sender):
        # if topic == self._node_id_ResetSignalArtefact_0+".get_activation_state":
        #     if message==ActivationState.ACTIVATED:
        #         self.reset_excl_event_checkBox.setChecked(True)
        #     if message==ActivationState.BYPASS:
        #         self.reset_excl_event_checkBox.setChecked(False)
        if topic == self._artefact_group_topic:
            if isinstance(message,dict):
                self.group_dict = message
            elif isinstance(message,str):
                self.group_dict = ast.literal_eval(message)
            self._set_event_lst_to_view()
        if topic == self._artefact_name_topic:   
            if isinstance(message,dict):
                self.name_dict = message
            elif isinstance(message,str):
                self.name_dict = ast.literal_eval(message)
            self._set_event_lst_to_view()


    # When the user pressed bush button "Apply to all files"
    def on_apply_to_all_files(self):
        # Extract the index of the selected file from the file list view
        file_index = self.file_listview.currentIndex()
        checkable_index = self.find_checkable_index(file_index)
        # Read the selected events for one file
            # group_list : list of string 
            # name_list : list of string          
        group_list, name_list = self.reader_settings_view.get_checked_event_lst_from_file(\
            self.files_check_event_model, checkable_index)
        # Uncheck all before applying the selection
        self.on_reset_all_files()                  
        # Apply the event list to all files
            # Set the CheckState to events listed in group_list and name_list
            #   group_list : list of string 
            #   name_list : list of string
            #   check_state : QtCore.Qt.CheckState
        n_files = len(self.reader_settings_view.get_files_list(self.files_check_event_model))
        n_events_to_find = len(group_list)
        evt_found_tab = np.zeros((n_files,n_events_to_find)) # Usefull to show a message of the events not found
        for i_file in range(n_files):
            index_file_model = self.files_check_event_model.index(i_file,0)
            # Set the CheckState to events listed in group_lst and name_list
            #   and returns evt_found_tab (array of number of events)
            #   usage : set_check_state_list(files_check_model, file_index, group_lst, name_list, check_state)            
            self.files_check_event_model, evt_found_tab[i_file, :] = self.reader_settings_view.set_check_state_list(\
                self.files_check_event_model, index_file_model, group_list, name_list, QtCore.Qt.CheckState.Checked)
        # Manage error message when the event is not found
        error_files = []
        if not evt_found_tab.all():
            for i_file, events_found in enumerate(evt_found_tab):
                if not events_found.all():
                    for i_event, event_found in enumerate(events_found):
                        if not event_found:
                            index_file_model = self.files_check_event_model.index(i_file,0)
                            file_item = self.files_check_event_model.itemFromIndex(index_file_model)
                            error_files.append((file_item.text(), group_list[i_event], name_list[i_event]))
            error_msg_pd = pd.DataFrame(data=error_files,columns=['file', 'group', 'name'])
            table_dialog_msg = TableDialog(df=error_msg_pd, title="Warning Message",message="Those events were not found", showDownloadButton=True)
            table_dialog_msg.exec_()
        # Read the event group and name from the model and update the local dict     
        # Saved selected states from self.files_check_event_model    
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()


    # Function to uncheck all groups and names.
    def on_reset_all_files(self):
        # Get the file list from the model
        n_files = len(self.reader_settings_view.get_files_list(self.files_check_event_model))
        # For each file of the list
        for i_file in range(n_files):
            file_index = self.files_check_event_model.index(i_file,0)
            # Set the CheckState to all groups and names of a file index selected
            #   set_check_state_file(index, check_state, model)
            #   and return the model updated
            self.files_check_event_model = self.reader_settings_view.set_check_state_file(\
                file_index, QtCore.Qt.CheckState.Unchecked, self.files_check_event_model)
        # Read the event group and name from the model and update the local dict           
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()


    # Called when the user clicks on RUN or when the pipeline is saved
    # Message are sent to the publisher   
    def on_apply_settings(self):
        # # Activate ResetSignalArtefact module if the excluded events signal is reset
        # if self.reset_excl_event_checkBox.isChecked():
        #     self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_0\
        #         +".activation_state_change", ActivationState.ACTIVATED)
        # else:
        #     self._pub_sub_manager.publish(self, self._node_id_ResetSignalArtefact_0\
        #         +".activation_state_change",ActivationState.BYPASS)
        # Read the event group and name from the model and update the local dict           
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()
        # send dictionaries to appropriate modules
        self._pub_sub_manager.publish(self, self._artefact_group_topic, str(self.group_dict))
        self._pub_sub_manager.publish(self, self._artefact_name_topic, str(self.name_dict))


    # Called when the user finish editing the search_event line edit
    def search_pattern_slot(self):
        self.event_proxy_model.invalidate()
        search_pattern = self.search_lineEdit.text()
        self.event_proxy_model.set_groups_search_pattern(search_pattern)


    # To read the local dicts in order to select the right events in the view.
    def _set_event_lst_to_view(self):
        if len(self.group_dict)>0 and len(self.name_dict)>0:
            # For each opened file
            for file_key in self.group_dict:
                # Extract which event groups and names are selected
                group_lst = self.group_dict[file_key]
                group_lst = group_lst.split(',')
                name_list = self.name_dict[file_key]
                name_list = name_list.split(',')
                # Find in the model the index of current filename
                view_index = self.reader_settings_view.get_file_index(file_key, self.files_model)
                # Set the view to the index of the file
                self.file_listview.setCurrentIndex(view_index)
                # Set the CheckState to events listed in group_lst and name_list
                #   and returns evt_found_tab (array of number of events)
                #   usage : set_check_state_list(files_check_model, file_index, group_lst, name_list, check_state)
                    # files_check_model : QtGui.QStandardItemModel
                    # file_index : QtCore.QModelIndex
                    # group_lst : list of string 
                    # name_list : list of string
                    # check_state : QtCore.Qt.CheckState
                file_check_index = self.find_checkable_index(view_index)
                #file_check_index = self.reader_settings_view.get_file_index(file_key, self.files_check_event_model)
                self.files_check_event_model, evt_found_tab = self.reader_settings_view.set_check_state_list(\
                    self.files_check_event_model, file_check_index, group_lst, name_list, QtCore.Qt.CheckState.Checked)


    # To read and save locally the selected events.
    # Read file list from the updated model (self.files_model) and 
    #   the states from the from the self.files_check_event_model 
    #   in order to send the information to the dictionary modules in the pipeline
    def _store_event_dict(self):       
        # Clean the local dictionary 
        group_dict = {}
        name_dict = {}
        # Get the file list from the model
        files_list = self.reader_settings_view.get_files_list(self.files_model)
        n_files = len(files_list)
        # For each file of the list
        for i_file in range(n_files):
            filename = files_list[i_file]
            file_index = self.reader_settings_view.get_file_index(filename, self.files_model)
            file_checkable_index = self.find_checkable_index(file_index)
            # If the file is new and will be added in the model
            if isinstance(file_checkable_index, list) and len(file_checkable_index)==0:
                group_dict[filename] = 'None'  # letting the field empty '' does not work
                name_dict[filename] = 'None'   # letting the field empty '' does not work
            elif isinstance(file_checkable_index, QtCore.QModelIndex):
                # group_lst and name_list are list of string 
                group_list, name_list = self.reader_settings_view.get_checked_event_lst_from_file(\
                    self.files_check_event_model, file_checkable_index)
                if len(group_list)>0:
                    # Construct the 2 local dicts: the key is the filename and the value is a string of groups or names
                    group_dict[filename] = ",".join(group_list) # string : groups separated by a comma
                    name_dict[filename] =  ",".join(name_list) # string : names separated by a comma
                else:
                    group_dict[filename] = 'None' # letting the field empty '' does not work
                    name_dict[filename] = 'None'  # letting the field empty '' does not work
            else:
                raise NodeRuntimeException(self.identifier, "_store_event_dict", \
                    f"NonValidEventStep : the selected index is not valid")

        return group_dict, name_dict


    # Called when the user checked\unchecked a group or a name
    # The input parameter item is the one changed
    def on_item_changed(self, item):
        # Disconnect the signal the time the states are analyzed and updated
        self.files_check_event_model.itemChanged.disconnect(self.on_item_changed)
        # If the user check/uncheck an event group propagate the state to children
        if item.hasChildren():
            self.files_check_event_model = self.reader_settings_view.apply_state_to_child_item(\
                item, self.files_check_event_model)
        # If the user check/uncheck an event name, 
        #   look the other names and propagate to the group
        else:
            item.setAutoTristate(False)
            # Set the parent state depending of children
            self.files_check_event_model = self.reader_settings_view.apply_state_to_parent_item(\
                item, self.files_check_event_model)
        # Update the self.group_dict and self.name_dict
        self.group_dict, self.name_dict = self._store_event_dict()
        # Connect the signal to listen to modification
        self.files_check_event_model.itemChanged.connect(self.on_item_changed)


    # Called when the user select a file in the PSG Files list
    def on_file_selected(self):
        # Extract file index selected, from the self.files_model
        file_index = self.file_listview.currentIndex()
        self.event_proxy_model.set_filenames_filters(file_index.data())
        # Map the index for the proxy model
        checkable_index = self.find_checkable_index(file_index)
        proxy_index = self.event_proxy_model.mapFromSource(checkable_index)
        self.event_treeview.setRootIndex(proxy_index)


    # Find the tree view index linked to the list view index
    def find_checkable_index(self, file_list_index):
        # Extract filename
        filename = file_list_index.data()
        # Get the file index for the self.files_check_event_model model
        file_check_item = self.files_check_event_model.findItems(\
            filename, flags=QtCore.Qt.MatchExactly, column=0)
        if len(file_check_item)>0:
            index = file_check_item[0].index()
            if isinstance(index, list):
                index = index[0]
        else:
            index = file_check_item
        return index


    # When the user checked/unchecked "Select all"
    def on_select_all_groups(self):
        # Extract how many event groups are available
        # Need to extract info from the proxy model since only the visible group has been selected all
        # How many rows available at the file_model pointer
        file_index = self.file_listview.currentIndex()
        proxy_index = self.event_proxy_model.mapFromSource(self.find_checkable_index(file_index))
        self.set_check_state_file_via_proxy(proxy_index, self.select_all_checkBox.checkState())
        # Read the event group and name from the model and update the local dict           
        # 2 dictionaries :
        # - group dictionary where the key is the filename and the item a string of groups
        # - name dictionary where the key is the filename and the item a string of names
        self.group_dict, self.name_dict = self._store_event_dict()
            

    def set_check_state_file_via_proxy(self, file_index, check_state):
        """
       Set the CheckState to all groups and names of a file index selected
        
        Parameters
        -----------
            file_index : QtCore.QModelIndex
            check_state : QtCore.Qt.CheckState
        """
        n_groups = self.event_proxy_model.rowCount(file_index)
        for group_row in range(n_groups):
            column = 0
            group_index = self.event_proxy_model.index(group_row, column, file_index)
            source_index = self.event_proxy_model.mapToSource(group_index)
            group_item = self.files_check_event_model.itemFromIndex(source_index)
            group_item.setCheckState(check_state)
            self.files_check_event_model = self.reader_settings_view.apply_state_to_child_item(\
                group_item, self.files_check_event_model)


    # Called when the user delete an instance of the plugin
    def __del__(self):
        if self._pub_sub_manager is not None:
            self._pub_sub_manager.unsubscribe(self, self._artefact_group_topic)
            self._pub_sub_manager.unsubscribe(self, self._artefact_name_topic)


    # Create the model for the checkable events tree, based on self.files_model
    # Update the self.group_dict and self.name_dict with the selected events
    #def update_checkable_model(self, group_dict_in, name_dict_in, checkable_model_outdated):
    def update_checkable_model(self, checkable_model_outdated):
        if checkable_model_outdated == None:
            # Create checkable item based on self.reader_settings_view.files_model
            #   events are not checked at this point
            files_check_event_model = self.reader_settings_view.create_files_model_checkable()
        else:
            # Add and remove only the modified file
            updated_file_list = self.reader_settings_view.get_files_list(self.files_model)
            outdated_file_list = self.reader_settings_view.get_files_list(checkable_model_outdated)
            # Finding missing filename in the outdated_file_list
            file_to_rem = [outdated_file for outdated_file in outdated_file_list if outdated_file not in updated_file_list]
            # pass through the new list of files and add the new files into the checkable_model_outdated
            for filename in updated_file_list:
                file_item = checkable_model_outdated.findItems(filename, flags=QtCore.Qt.MatchExactly, column=0)
                # If it is a new file -> add it
                if len(file_item)==0:
                    # tree item : parent=file, child=group and count, child=name and count
                    item = self.reader_settings_view.create_file_item_count(filename, True)
                    checkable_model_outdated.appendRow(item)
                # Otherwise -> nothing to do
            # remove the files from checkable_model_outdated
            if len(file_to_rem):
                checkable_model_outdated = self.remove_files(file_to_rem, checkable_model_outdated)
            files_check_event_model = checkable_model_outdated
        return files_check_event_model#, group_dict_out, name_dict_out


    def remove_files(self, file_to_rem, model):
        # Pass through the files to remove row for each column
        column=0
        row_to_rem = []
        for filename in file_to_rem :
            file_item = model.findItems(filename, flags=QtCore.Qt.MatchExactly, column=column)
            row_to_rem.append(file_item[0].row())
        # Remove the last first to avoid changing the index file
        row_to_rem.sort(reverse=True)
        for row in row_to_rem:
            model.removeRow(row)
        return model