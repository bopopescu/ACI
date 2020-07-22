""" Cisco_IOS_XR_lib_keychain_act 

This module contains a collection of YANG definitions
for Cisco IOS\-XR action package configuration.

Copyright (c) 2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class MainKeyAdd(Entity):
    """
    To add a new main key
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act.MainKeyAdd.Input>`
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MainKeyAdd, self).__init__()
        self._top_entity = None

        self.yang_name = "main-key-add"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = MainKeyAdd.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-act:main-key-add"


    class Input(Entity):
        """
        
        
        .. attribute:: new_key
        
        	New main key to be added
        	**type**\: str
        
        

        """

        _prefix = 'lib-keychain-act'
        _revision = '2017-04-17'

        def __init__(self):
            super(MainKeyAdd.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "main-key-add"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('new_key', YLeaf(YType.str, 'new-key')),
            ])
            self.new_key = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-act:main-key-add/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MainKeyAdd.Input, ['new_key'], name, value)

    def clone_ptr(self):
        self._top_entity = MainKeyAdd()
        return self._top_entity

class MainKeyDelete(Entity):
    """
    Remove Main key
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MainKeyDelete, self).__init__()
        self._top_entity = None

        self.yang_name = "main-key-delete"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-act:main-key-delete"

    def clone_ptr(self):
        self._top_entity = MainKeyDelete()
        return self._top_entity

class MainKeyUpdate(Entity):
    """
    To update main key
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xr.Cisco_IOS_XR_lib_keychain_act.MainKeyUpdate.Input>`
    
    

    """

    _prefix = 'lib-keychain-act'
    _revision = '2017-04-17'

    def __init__(self):
        super(MainKeyUpdate, self).__init__()
        self._top_entity = None

        self.yang_name = "main-key-update"
        self.yang_parent_name = "Cisco-IOS-XR-lib-keychain-act"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = MainKeyUpdate.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")
        self._segment_path = lambda: "Cisco-IOS-XR-lib-keychain-act:main-key-update"


    class Input(Entity):
        """
        
        
        .. attribute:: old_key
        
        	key already added/key to be replaced
        	**type**\: str
        
        	**mandatory**\: True
        
        .. attribute:: new_key
        
        	New main key to be added 
        	**type**\: str
        
        	**mandatory**\: True
        
        

        """

        _prefix = 'lib-keychain-act'
        _revision = '2017-04-17'

        def __init__(self):
            super(MainKeyUpdate.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "main-key-update"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('old_key', YLeaf(YType.str, 'old-key')),
                ('new_key', YLeaf(YType.str, 'new-key')),
            ])
            self.old_key = None
            self.new_key = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "Cisco-IOS-XR-lib-keychain-act:main-key-update/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(MainKeyUpdate.Input, ['old_key', 'new_key'], name, value)

    def clone_ptr(self):
        self._top_entity = MainKeyUpdate()
        return self._top_entity

