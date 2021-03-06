""" Cisco_IOS_XR_tunnel_l2tun_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR tunnel\-l2tun package configuration.

This module contains definitions
for the following management objects\:
  l2tp\: L2TPv3 class used for L2VPNs

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class L2tpDigestHashMethod(Enum):
    """
    L2tpDigestHashMethod (Enum Class)

    L2tp digest hash method

    .. data:: md5 = 1

    	MD5

    .. data:: sha1 = 2

    	SHA1

    """

    md5 = Enum.YLeaf(1, "md5")

    sha1 = Enum.YLeaf(2, "sha1")


class L2tpHashMethod(Enum):
    """
    L2tpHashMethod (Enum Class)

    L2tp hash method

    .. data:: md5 = 1

    	MD5

    .. data:: sha1 = 2

    	SHA1

    .. data:: none = 3

    	None

    """

    md5 = Enum.YLeaf(1, "md5")

    sha1 = Enum.YLeaf(2, "sha1")

    none = Enum.YLeaf(3, "none")



class L2Tp(Entity):
    """
    L2TPv3 class used for L2VPNs
    
    .. attribute:: classes
    
    	List of classes
    	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes>`
    
    

    """

    _prefix = 'tunnel-l2tun-cfg'
    _revision = '2015-11-09'

    def __init__(self):
        super(L2Tp, self).__init__()
        self._top_entity = None

        self.yang_name = "l2tp"
        self.yang_parent_name = "Cisco-IOS-XR-tunnel-l2tun-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("classes", ("classes", L2Tp.Classes))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.classes = L2Tp.Classes()
        self.classes.parent = self
        self._children_name_map["classes"] = "classes"
        self._children_yang_names.add("classes")
        self._segment_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp"


    class Classes(Entity):
        """
        List of classes
        
        .. attribute:: class_
        
        	Configuration for a specific class
        	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class>`
        
        

        """

        _prefix = 'tunnel-l2tun-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(L2Tp.Classes, self).__init__()

            self.yang_name = "classes"
            self.yang_parent_name = "l2tp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("class", ("class_", L2Tp.Classes.Class))])
            self._leafs = OrderedDict()

            self.class_ = YList(self)
            self._segment_path = lambda: "classes"
            self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(L2Tp.Classes, [], name, value)


        class Class(Entity):
            """
            Configuration for a specific class
            
            .. attribute:: class_name  (key)
            
            	Specify the class name. Regexp\: ^[a\-z0\-9A\-Z][\-\_.a\-z0\-9A\-Z]\*$
            	**type**\: str
            
            	**length:** 1..31
            
            .. attribute:: security
            
            	Security check
            	**type**\:  :py:class:`Security <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Security>`
            
            .. attribute:: retransmit
            
            	Control message retransmission parameters
            	**type**\:  :py:class:`Retransmit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Retransmit>`
            
            .. attribute:: tunnel
            
            	l2TP tunnel
            	**type**\:  :py:class:`Tunnel <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Tunnel>`
            
            .. attribute:: digest
            
            	Message digest authentication for the L2TP control connection
            	**type**\:  :py:class:`Digest <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Digest>`
            
            .. attribute:: ip
            
            	IP TOS value
            	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Ip>`
            
            .. attribute:: host_name
            
            	Local hostname for control connection authentication
            	**type**\: str
            
            .. attribute:: hidden
            
            	Specify to hide AVPs in outgoing control messages
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: hello_interval
            
            	Specify interval (in seconds)
            	**type**\: int
            
            	**range:** 0..1000
            
            	**units**\: second
            
            .. attribute:: timeout_setup
            
            	Time permitted to set up a control connection
            	**type**\: int
            
            	**range:** 60..6000
            
            	**units**\: second
            
            .. attribute:: receive_window
            
            	Receive window size for the control connection
            	**type**\: int
            
            	**range:** 1..16384
            
            	**units**\: byte
            
            .. attribute:: congestion_control
            
            	Congestion control enabled
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: timeout_no_user
            
            	Timeout value for no\-user in seconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**units**\: second
            
            .. attribute:: authentication
            
            	Authenticate the L2TP control connection
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: enable
            
            	Enable L2TPv3 class used for L2VPNs
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: password
            
            	Specify the password for control channel authentication
            	**type**\: str
            
            	**pattern:** (!.+)\|([^!].+)
            
            

            """

            _prefix = 'tunnel-l2tun-cfg'
            _revision = '2015-11-09'

            def __init__(self):
                super(L2Tp.Classes.Class, self).__init__()

                self.yang_name = "class"
                self.yang_parent_name = "classes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['class_name']
                self._child_container_classes = OrderedDict([("security", ("security", L2Tp.Classes.Class.Security)), ("retransmit", ("retransmit", L2Tp.Classes.Class.Retransmit)), ("tunnel", ("tunnel", L2Tp.Classes.Class.Tunnel)), ("digest", ("digest", L2Tp.Classes.Class.Digest)), ("ip", ("ip", L2Tp.Classes.Class.Ip))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('class_name', YLeaf(YType.str, 'class-name')),
                    ('host_name', YLeaf(YType.str, 'host-name')),
                    ('hidden', YLeaf(YType.empty, 'hidden')),
                    ('hello_interval', YLeaf(YType.uint32, 'hello-interval')),
                    ('timeout_setup', YLeaf(YType.uint32, 'timeout-setup')),
                    ('receive_window', YLeaf(YType.uint32, 'receive-window')),
                    ('congestion_control', YLeaf(YType.empty, 'congestion-control')),
                    ('timeout_no_user', YLeaf(YType.uint32, 'timeout-no-user')),
                    ('authentication', YLeaf(YType.int32, 'authentication')),
                    ('enable', YLeaf(YType.empty, 'enable')),
                    ('password', YLeaf(YType.str, 'password')),
                ])
                self.class_name = None
                self.host_name = None
                self.hidden = None
                self.hello_interval = None
                self.timeout_setup = None
                self.receive_window = None
                self.congestion_control = None
                self.timeout_no_user = None
                self.authentication = None
                self.enable = None
                self.password = None

                self.security = L2Tp.Classes.Class.Security()
                self.security.parent = self
                self._children_name_map["security"] = "security"
                self._children_yang_names.add("security")

                self.retransmit = L2Tp.Classes.Class.Retransmit()
                self.retransmit.parent = self
                self._children_name_map["retransmit"] = "retransmit"
                self._children_yang_names.add("retransmit")

                self.tunnel = L2Tp.Classes.Class.Tunnel()
                self.tunnel.parent = self
                self._children_name_map["tunnel"] = "tunnel"
                self._children_yang_names.add("tunnel")

                self.digest = L2Tp.Classes.Class.Digest()
                self.digest.parent = self
                self._children_name_map["digest"] = "digest"
                self._children_yang_names.add("digest")

                self.ip = L2Tp.Classes.Class.Ip()
                self.ip.parent = self
                self._children_name_map["ip"] = "ip"
                self._children_yang_names.add("ip")
                self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-tunnel-l2tun-cfg:l2tp/classes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(L2Tp.Classes.Class, ['class_name', 'host_name', 'hidden', 'hello_interval', 'timeout_setup', 'receive_window', 'congestion_control', 'timeout_no_user', 'authentication', 'enable', 'password'], name, value)


            class Security(Entity):
                """
                Security check
                
                .. attribute:: ip
                
                	Security check for IP
                	**type**\:  :py:class:`Ip <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Security.Ip>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class.Security, self).__init__()

                    self.yang_name = "security"
                    self.yang_parent_name = "class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("ip", ("ip", L2Tp.Classes.Class.Security.Ip))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.ip = L2Tp.Classes.Class.Security.Ip()
                    self.ip.parent = self
                    self._children_name_map["ip"] = "ip"
                    self._children_yang_names.add("ip")
                    self._segment_path = lambda: "security"


                class Ip(Entity):
                    """
                    Security check for IP
                    
                    .. attribute:: address_check
                    
                    	Enable IP address check for L2TP packets
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class.Security.Ip, self).__init__()

                        self.yang_name = "ip"
                        self.yang_parent_name = "security"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address_check', YLeaf(YType.empty, 'address-check')),
                        ])
                        self.address_check = None
                        self._segment_path = lambda: "ip"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Classes.Class.Security.Ip, ['address_check'], name, value)


            class Retransmit(Entity):
                """
                Control message retransmission parameters
                
                .. attribute:: initial
                
                	Set retries and timeouts for initial
                	**type**\:  :py:class:`Initial <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Retransmit.Initial>`
                
                .. attribute:: retry
                
                	Specify retransmit retry count
                	**type**\: int
                
                	**range:** 5..1000
                
                .. attribute:: timeout
                
                	Set timeout value range
                	**type**\:  :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Retransmit.Timeout>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class.Retransmit, self).__init__()

                    self.yang_name = "retransmit"
                    self.yang_parent_name = "class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("initial", ("initial", L2Tp.Classes.Class.Retransmit.Initial)), ("timeout", ("timeout", L2Tp.Classes.Class.Retransmit.Timeout))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('retry', YLeaf(YType.uint32, 'retry')),
                    ])
                    self.retry = None

                    self.initial = L2Tp.Classes.Class.Retransmit.Initial()
                    self.initial.parent = self
                    self._children_name_map["initial"] = "initial"
                    self._children_yang_names.add("initial")

                    self.timeout = L2Tp.Classes.Class.Retransmit.Timeout()
                    self.timeout.parent = self
                    self._children_name_map["timeout"] = "timeout"
                    self._children_yang_names.add("timeout")
                    self._segment_path = lambda: "retransmit"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.Classes.Class.Retransmit, ['retry'], name, value)


                class Initial(Entity):
                    """
                    Set retries and timeouts for initial
                    
                    .. attribute:: retry
                    
                    	Specify the retry number
                    	**type**\: int
                    
                    	**range:** 1..1000
                    
                    .. attribute:: timeout
                    
                    	Set timeout value range
                    	**type**\:  :py:class:`Timeout <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Retransmit.Initial.Timeout>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class.Retransmit.Initial, self).__init__()

                        self.yang_name = "initial"
                        self.yang_parent_name = "retransmit"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([("timeout", ("timeout", L2Tp.Classes.Class.Retransmit.Initial.Timeout))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('retry', YLeaf(YType.uint32, 'retry')),
                        ])
                        self.retry = None

                        self.timeout = L2Tp.Classes.Class.Retransmit.Initial.Timeout()
                        self.timeout.parent = self
                        self._children_name_map["timeout"] = "timeout"
                        self._children_yang_names.add("timeout")
                        self._segment_path = lambda: "initial"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Classes.Class.Retransmit.Initial, ['retry'], name, value)


                    class Timeout(Entity):
                        """
                        Set timeout value range
                        
                        .. attribute:: minimum
                        
                        	Specify minimum timeout
                        	**type**\: int
                        
                        	**range:** 1..8
                        
                        .. attribute:: maximum
                        
                        	Specify maximum timeout
                        	**type**\: int
                        
                        	**range:** 1..8
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Classes.Class.Retransmit.Initial.Timeout, self).__init__()

                            self.yang_name = "timeout"
                            self.yang_parent_name = "initial"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('minimum', YLeaf(YType.uint32, 'minimum')),
                                ('maximum', YLeaf(YType.uint32, 'maximum')),
                            ])
                            self.minimum = None
                            self.maximum = None
                            self._segment_path = lambda: "timeout"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Classes.Class.Retransmit.Initial.Timeout, ['minimum', 'maximum'], name, value)


                class Timeout(Entity):
                    """
                    Set timeout value range
                    
                    .. attribute:: minimum
                    
                    	Specify minimum timeout
                    	**type**\: int
                    
                    	**range:** 1..8
                    
                    .. attribute:: maximum
                    
                    	Specify maximum timeout
                    	**type**\: int
                    
                    	**range:** 1..8
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class.Retransmit.Timeout, self).__init__()

                        self.yang_name = "timeout"
                        self.yang_parent_name = "retransmit"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('minimum', YLeaf(YType.uint32, 'minimum')),
                            ('maximum', YLeaf(YType.uint32, 'maximum')),
                        ])
                        self.minimum = None
                        self.maximum = None
                        self._segment_path = lambda: "timeout"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Classes.Class.Retransmit.Timeout, ['minimum', 'maximum'], name, value)


            class Tunnel(Entity):
                """
                l2TP tunnel
                
                .. attribute:: accounting
                
                	Tunnel accounting
                	**type**\: str
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class.Tunnel, self).__init__()

                    self.yang_name = "tunnel"
                    self.yang_parent_name = "class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('accounting', YLeaf(YType.str, 'accounting')),
                    ])
                    self.accounting = None
                    self._segment_path = lambda: "tunnel"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.Classes.Class.Tunnel, ['accounting'], name, value)


            class Digest(Entity):
                """
                Message digest authentication for the L2TP
                control connection
                
                .. attribute:: secrets
                
                	Set shared secret for message digest
                	**type**\:  :py:class:`Secrets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Digest.Secrets>`
                
                .. attribute:: hash
                
                	Specify hash method
                	**type**\:  :py:class:`L2tpDigestHashMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2tpDigestHashMethod>`
                
                .. attribute:: check_disable
                
                	Disable digest checking
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class.Digest, self).__init__()

                    self.yang_name = "digest"
                    self.yang_parent_name = "class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("secrets", ("secrets", L2Tp.Classes.Class.Digest.Secrets))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hash', YLeaf(YType.enumeration, 'hash')),
                        ('check_disable', YLeaf(YType.empty, 'check-disable')),
                    ])
                    self.hash = None
                    self.check_disable = None

                    self.secrets = L2Tp.Classes.Class.Digest.Secrets()
                    self.secrets.parent = self
                    self._children_name_map["secrets"] = "secrets"
                    self._children_yang_names.add("secrets")
                    self._segment_path = lambda: "digest"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.Classes.Class.Digest, ['hash', 'check_disable'], name, value)


                class Secrets(Entity):
                    """
                    Set shared secret for message digest
                    
                    .. attribute:: secret
                    
                    	The encrypted user secret and hash method
                    	**type**\: list of  		 :py:class:`Secret <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2Tp.Classes.Class.Digest.Secrets.Secret>`
                    
                    

                    """

                    _prefix = 'tunnel-l2tun-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(L2Tp.Classes.Class.Digest.Secrets, self).__init__()

                        self.yang_name = "secrets"
                        self.yang_parent_name = "digest"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("secret", ("secret", L2Tp.Classes.Class.Digest.Secrets.Secret))])
                        self._leafs = OrderedDict()

                        self.secret = YList(self)
                        self._segment_path = lambda: "secrets"

                    def __setattr__(self, name, value):
                        self._perform_setattr(L2Tp.Classes.Class.Digest.Secrets, [], name, value)


                    class Secret(Entity):
                        """
                        The encrypted user secret and hash method
                        
                        .. attribute:: secret_name  (key)
                        
                        	Specify the encrypted user secret
                        	**type**\: str
                        
                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                        
                        .. attribute:: hash
                        
                        	Specify hash method
                        	**type**\:  :py:class:`L2tpHashMethod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_tunnel_l2tun_cfg.L2tpHashMethod>`
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'tunnel-l2tun-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(L2Tp.Classes.Class.Digest.Secrets.Secret, self).__init__()

                            self.yang_name = "secret"
                            self.yang_parent_name = "secrets"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['secret_name']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('secret_name', YLeaf(YType.str, 'secret-name')),
                                ('hash', YLeaf(YType.enumeration, 'hash')),
                            ])
                            self.secret_name = None
                            self.hash = None
                            self._segment_path = lambda: "secret" + "[secret-name='" + str(self.secret_name) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(L2Tp.Classes.Class.Digest.Secrets.Secret, ['secret_name', 'hash'], name, value)


            class Ip(Entity):
                """
                IP TOS value
                
                .. attribute:: tos
                
                	IP TOS value (decimal)
                	**type**\: int
                
                	**range:** 0..255
                
                

                """

                _prefix = 'tunnel-l2tun-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(L2Tp.Classes.Class.Ip, self).__init__()

                    self.yang_name = "ip"
                    self.yang_parent_name = "class"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('tos', YLeaf(YType.uint32, 'tos')),
                    ])
                    self.tos = None
                    self._segment_path = lambda: "ip"

                def __setattr__(self, name, value):
                    self._perform_setattr(L2Tp.Classes.Class.Ip, ['tos'], name, value)

    def clone_ptr(self):
        self._top_entity = L2Tp()
        return self._top_entity

