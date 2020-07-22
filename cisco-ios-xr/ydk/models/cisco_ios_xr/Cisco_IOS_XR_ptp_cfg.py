""" Cisco_IOS_XR_ptp_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ptp package configuration.

This module contains definitions
for the following management objects\:
  ptp\: PTP global configuration

This YANG module augments the
  Cisco\-IOS\-XR\-ifmgr\-cfg
module with configuration data.

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class Ptp(Entity):
    """
    PTP global configuration
    
    .. attribute:: clock
    
    	PTP local clock configuration
    	**type**\:  :py:class:`Clock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Clock>`
    
    .. attribute:: profiles
    
    	Table for profile configuration
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles>`
    
    .. attribute:: utc_offset
    
    	UTC offset configuration
    	**type**\:  :py:class:`UtcOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset>`
    
    .. attribute:: logging
    
    	PTP logging configuration
    	**type**\:  :py:class:`Logging <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Logging>`
    
    .. attribute:: transparent_clock
    
    	Transparent clock configuration
    	**type**\:  :py:class:`TransparentClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.TransparentClock>`
    
    .. attribute:: time_of_day_priority
    
    	Time\-of\-day priority
    	**type**\: int
    
    	**range:** 1..254
    
    	**default value**\: 100
    
    .. attribute:: frequency_priority
    
    	Frequency priority
    	**type**\: int
    
    	**range:** 1..254
    
    	**default value**\: 254
    
    .. attribute:: startup_clock_class
    
    	Startup clock class value
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: enable
    
    	Enable the precision time protocol
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: min_clock_class
    
    	Clocks with a clock\-class higher than the minimum clock class will not be considered for selection as a parent clock
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: uncalibrated_clock_class
    
    	Clock class to be used while acquiring phase\-lock to a parent clock
    	**type**\: int
    
    	**range:** 0..255
    
    .. attribute:: freerun_clock_class
    
    	Freerun clock class value
    	**type**\: int
    
    	**range:** 0..255
    
    

    """

    _prefix = 'ptp-cfg'
    _revision = '2017-02-02'

    def __init__(self):
        super(Ptp, self).__init__()
        self._top_entity = None

        self.yang_name = "ptp"
        self.yang_parent_name = "Cisco-IOS-XR-ptp-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("clock", ("clock", Ptp.Clock)), ("profiles", ("profiles", Ptp.Profiles)), ("utc-offset", ("utc_offset", Ptp.UtcOffset)), ("logging", ("logging", Ptp.Logging)), ("transparent-clock", ("transparent_clock", Ptp.TransparentClock))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict([
            ('time_of_day_priority', YLeaf(YType.uint32, 'time-of-day-priority')),
            ('frequency_priority', YLeaf(YType.uint32, 'frequency-priority')),
            ('startup_clock_class', YLeaf(YType.uint32, 'startup-clock-class')),
            ('enable', YLeaf(YType.empty, 'enable')),
            ('min_clock_class', YLeaf(YType.uint32, 'min-clock-class')),
            ('uncalibrated_clock_class', YLeaf(YType.uint32, 'uncalibrated-clock-class')),
            ('freerun_clock_class', YLeaf(YType.uint32, 'freerun-clock-class')),
        ])
        self.time_of_day_priority = None
        self.frequency_priority = None
        self.startup_clock_class = None
        self.enable = None
        self.min_clock_class = None
        self.uncalibrated_clock_class = None
        self.freerun_clock_class = None

        self.clock = Ptp.Clock()
        self.clock.parent = self
        self._children_name_map["clock"] = "clock"
        self._children_yang_names.add("clock")

        self.profiles = Ptp.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"
        self._children_yang_names.add("profiles")

        self.utc_offset = Ptp.UtcOffset()
        self.utc_offset.parent = self
        self._children_name_map["utc_offset"] = "utc-offset"
        self._children_yang_names.add("utc-offset")

        self.logging = Ptp.Logging()
        self.logging.parent = self
        self._children_name_map["logging"] = "logging"
        self._children_yang_names.add("logging")

        self.transparent_clock = Ptp.TransparentClock()
        self.transparent_clock.parent = self
        self._children_name_map["transparent_clock"] = "transparent-clock"
        self._children_yang_names.add("transparent-clock")
        self._segment_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp"

    def __setattr__(self, name, value):
        self._perform_setattr(Ptp, ['time_of_day_priority', 'frequency_priority', 'startup_clock_class', 'enable', 'min_clock_class', 'uncalibrated_clock_class', 'freerun_clock_class'], name, value)


    class Clock(Entity):
        """
        PTP local clock configuration
        
        .. attribute:: profile
        
        	Local clock PTP profile
        	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Clock.Profile>`
        
        .. attribute:: identity
        
        	Local clock identity
        	**type**\:  :py:class:`Identity <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Clock.Identity>`
        
        .. attribute:: timescale
        
        	Local clock timescale
        	**type**\:  :py:class:`PtpTimescale <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimescale>`
        
        .. attribute:: domain
        
        	Local clock domain
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 0
        
        .. attribute:: priority2
        
        	Local clock priority2
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 128
        
        .. attribute:: time_source
        
        	Local clock time source
        	**type**\:  :py:class:`PtpTimeSource <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimeSource>`
        
        .. attribute:: priority1
        
        	Local clock priority1
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 128
        
        .. attribute:: clock_class
        
        	Local clock class
        	**type**\: int
        
        	**range:** 0..255
        
        	**default value**\: 0
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Clock, self).__init__()

            self.yang_name = "clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("profile", ("profile", Ptp.Clock.Profile)), ("identity", ("identity", Ptp.Clock.Identity))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('timescale', YLeaf(YType.enumeration, 'timescale')),
                ('domain', YLeaf(YType.uint32, 'domain')),
                ('priority2', YLeaf(YType.uint32, 'priority2')),
                ('time_source', YLeaf(YType.enumeration, 'time-source')),
                ('priority1', YLeaf(YType.uint32, 'priority1')),
                ('clock_class', YLeaf(YType.uint32, 'clock-class')),
            ])
            self.timescale = None
            self.domain = None
            self.priority2 = None
            self.time_source = None
            self.priority1 = None
            self.clock_class = None

            self.profile = Ptp.Clock.Profile()
            self.profile.parent = self
            self._children_name_map["profile"] = "profile"
            self._children_yang_names.add("profile")

            self.identity = Ptp.Clock.Identity()
            self.identity.parent = self
            self._children_name_map["identity"] = "identity"
            self._children_yang_names.add("identity")
            self._segment_path = lambda: "clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Clock, ['timescale', 'domain', 'priority2', 'time_source', 'priority1', 'clock_class'], name, value)


        class Profile(Entity):
            """
            Local clock PTP profile
            
            .. attribute:: clock_profile
            
            	Clock profile
            	**type**\:  :py:class:`PtpClockProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockProfile>`
            
            	**default value**\: default
            
            .. attribute:: telecom_clock_type
            
            	Telecom clock type
            	**type**\:  :py:class:`PtpTelecomClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTelecomClock>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Clock.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clock_profile', YLeaf(YType.enumeration, 'clock-profile')),
                    ('telecom_clock_type', YLeaf(YType.enumeration, 'telecom-clock-type')),
                ])
                self.clock_profile = None
                self.telecom_clock_type = None
                self._segment_path = lambda: "profile"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Clock.Profile, ['clock_profile', 'telecom_clock_type'], name, value)


        class Identity(Entity):
            """
            Local clock identity
            
            .. attribute:: clock_id_type
            
            	Clock identity type
            	**type**\:  :py:class:`PtpClockId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockId>`
            
            	**default value**\: router-mac
            
            .. attribute:: mac_address
            
            	MAC Address
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            .. attribute:: eui
            
            	EUI\-64 number
            	**type**\: str
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Clock.Identity, self).__init__()

                self.yang_name = "identity"
                self.yang_parent_name = "clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('clock_id_type', YLeaf(YType.enumeration, 'clock-id-type')),
                    ('mac_address', YLeaf(YType.str, 'mac-address')),
                    ('eui', YLeaf(YType.str, 'eui')),
                ])
                self.clock_id_type = None
                self.mac_address = None
                self.eui = None
                self._segment_path = lambda: "identity"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Clock.Identity, ['clock_id_type', 'mac_address', 'eui'], name, value)


    class Profiles(Entity):
        """
        Table for profile configuration
        
        .. attribute:: profile
        
        	Profile configuration
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile>`
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("profile", ("profile", Ptp.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.Profiles, [], name, value)


        class Profile(Entity):
            """
            Profile configuration
            
            .. attribute:: profile_name  (key)
            
            	Profile
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: announce_interval
            
            	Announce interval
            	**type**\:  :py:class:`AnnounceInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.AnnounceInterval>`
            
            .. attribute:: source_ipv4_address
            
            	Source IPv4 Address
            	**type**\:  :py:class:`SourceIpv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.SourceIpv4Address>`
            
            .. attribute:: subordinates
            
            	Table for subordinate configuration
            	**type**\:  :py:class:`Subordinates <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Subordinates>`
            
            .. attribute:: sync_interval
            
            	Sync interval
            	**type**\:  :py:class:`SyncInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.SyncInterval>`
            
            .. attribute:: mains
            
            	Table for main configuration
            	**type**\:  :py:class:`Mains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Mains>`
            
            .. attribute:: communication
            
            	Communication model
            	**type**\:  :py:class:`Communication <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Communication>`
            
            .. attribute:: delay_request_minimum_interval
            
            	Minimum delay request interval
            	**type**\:  :py:class:`DelayRequestMinimumInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.DelayRequestMinimumInterval>`
            
            .. attribute:: source_ipv6_address
            
            	Source IPv6 Address
            	**type**\:  :py:class:`SourceIpv6Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.SourceIpv6Address>`
            
            .. attribute:: sync_grant_duration
            
            	Sync unicast grant duration, in seconds
            	**type**\: int
            
            	**range:** 60..1000
            
            	**units**\: second
            
            	**default value**\: 300
            
            .. attribute:: general_cos
            
            	General COS
            	**type**\: int
            
            	**range:** 0..7
            
            	**default value**\: 6
            
            .. attribute:: sync_timeout
            
            	Sync timeout, in milliseconds
            	**type**\: int
            
            	**range:** 100..100000
            
            	**units**\: millisecond
            
            	**default value**\: 5000
            
            .. attribute:: transport
            
            	Transport
            	**type**\:  :py:class:`PtpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpEncap>`
            
            	**default value**\: ipv4
            
            .. attribute:: announce_timeout
            
            	Announce Timeout
            	**type**\: int
            
            	**range:** 2..10
            
            	**default value**\: 3
            
            .. attribute:: cos
            
            	COS
            	**type**\: int
            
            	**range:** 0..7
            
            	**default value**\: 6
            
            .. attribute:: port_state
            
            	Port state restriction
            	**type**\:  :py:class:`PtpPortState <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpPortState>`
            
            	**default value**\: any
            
            .. attribute:: delay_response_timeout
            
            	Delay\-Response timeout, in milliseconds
            	**type**\: int
            
            	**range:** 100..100000
            
            	**units**\: millisecond
            
            	**default value**\: 5000
            
            .. attribute:: delay_response_grant_duration
            
            	Delay\-Response unicast grant duration, in seconds
            	**type**\: int
            
            	**range:** 60..1000
            
            	**units**\: second
            
            	**default value**\: 300
            
            .. attribute:: event_cos
            
            	Event COS
            	**type**\: int
            
            	**range:** 0..7
            
            	**default value**\: 6
            
            .. attribute:: dscp
            
            	DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            	**default value**\: 46
            
            .. attribute:: general_dscp
            
            	General DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            	**default value**\: 46
            
            .. attribute:: clock_operation
            
            	Clock Operation
            	**type**\:  :py:class:`PtpClockOperation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpClockOperation>`
            
            	**default value**\: two-step
            
            .. attribute:: announce_grant_duration
            
            	Announce unicast grant duration, in seconds
            	**type**\: int
            
            	**range:** 60..1000
            
            	**units**\: second
            
            	**default value**\: 300
            
            .. attribute:: unicast_grant_invalid_request
            
            	Invalid unicast grant request response
            	**type**\:  :py:class:`PtpInvalidUnicastGrantRequestResponse <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpInvalidUnicastGrantRequestResponse>`
            
            	**default value**\: reduce
            
            .. attribute:: event_dscp
            
            	Event DSCP
            	**type**\: int
            
            	**range:** 0..63
            
            	**default value**\: 46
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['profile_name']
                self._child_container_classes = OrderedDict([("announce-interval", ("announce_interval", Ptp.Profiles.Profile.AnnounceInterval)), ("source-ipv4-address", ("source_ipv4_address", Ptp.Profiles.Profile.SourceIpv4Address)), ("subordinates", ("subordinates", Ptp.Profiles.Profile.Subordinates)), ("sync-interval", ("sync_interval", Ptp.Profiles.Profile.SyncInterval)), ("mains", ("mains", Ptp.Profiles.Profile.Mains)), ("communication", ("communication", Ptp.Profiles.Profile.Communication)), ("delay-request-minimum-interval", ("delay_request_minimum_interval", Ptp.Profiles.Profile.DelayRequestMinimumInterval)), ("source-ipv6-address", ("source_ipv6_address", Ptp.Profiles.Profile.SourceIpv6Address))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                    ('sync_grant_duration', YLeaf(YType.uint32, 'sync-grant-duration')),
                    ('general_cos', YLeaf(YType.uint32, 'general-cos')),
                    ('sync_timeout', YLeaf(YType.uint32, 'sync-timeout')),
                    ('transport', YLeaf(YType.enumeration, 'transport')),
                    ('announce_timeout', YLeaf(YType.uint32, 'announce-timeout')),
                    ('cos', YLeaf(YType.uint32, 'cos')),
                    ('port_state', YLeaf(YType.enumeration, 'port-state')),
                    ('delay_response_timeout', YLeaf(YType.uint32, 'delay-response-timeout')),
                    ('delay_response_grant_duration', YLeaf(YType.uint32, 'delay-response-grant-duration')),
                    ('event_cos', YLeaf(YType.uint32, 'event-cos')),
                    ('dscp', YLeaf(YType.uint32, 'dscp')),
                    ('general_dscp', YLeaf(YType.uint32, 'general-dscp')),
                    ('clock_operation', YLeaf(YType.enumeration, 'clock-operation')),
                    ('announce_grant_duration', YLeaf(YType.uint32, 'announce-grant-duration')),
                    ('unicast_grant_invalid_request', YLeaf(YType.enumeration, 'unicast-grant-invalid-request')),
                    ('event_dscp', YLeaf(YType.uint32, 'event-dscp')),
                ])
                self.profile_name = None
                self.sync_grant_duration = None
                self.general_cos = None
                self.sync_timeout = None
                self.transport = None
                self.announce_timeout = None
                self.cos = None
                self.port_state = None
                self.delay_response_timeout = None
                self.delay_response_grant_duration = None
                self.event_cos = None
                self.dscp = None
                self.general_dscp = None
                self.clock_operation = None
                self.announce_grant_duration = None
                self.unicast_grant_invalid_request = None
                self.event_dscp = None

                self.announce_interval = Ptp.Profiles.Profile.AnnounceInterval()
                self.announce_interval.parent = self
                self._children_name_map["announce_interval"] = "announce-interval"
                self._children_yang_names.add("announce-interval")

                self.source_ipv4_address = Ptp.Profiles.Profile.SourceIpv4Address()
                self.source_ipv4_address.parent = self
                self._children_name_map["source_ipv4_address"] = "source-ipv4-address"
                self._children_yang_names.add("source-ipv4-address")

                self.subordinates = Ptp.Profiles.Profile.Subordinates()
                self.subordinates.parent = self
                self._children_name_map["subordinates"] = "subordinates"
                self._children_yang_names.add("subordinates")

                self.sync_interval = Ptp.Profiles.Profile.SyncInterval()
                self.sync_interval.parent = self
                self._children_name_map["sync_interval"] = "sync-interval"
                self._children_yang_names.add("sync-interval")

                self.mains = Ptp.Profiles.Profile.Mains()
                self.mains.parent = self
                self._children_name_map["mains"] = "mains"
                self._children_yang_names.add("mains")

                self.communication = Ptp.Profiles.Profile.Communication()
                self.communication.parent = self
                self._children_name_map["communication"] = "communication"
                self._children_yang_names.add("communication")

                self.delay_request_minimum_interval = Ptp.Profiles.Profile.DelayRequestMinimumInterval()
                self.delay_request_minimum_interval.parent = self
                self._children_name_map["delay_request_minimum_interval"] = "delay-request-minimum-interval"
                self._children_yang_names.add("delay-request-minimum-interval")

                self.source_ipv6_address = Ptp.Profiles.Profile.SourceIpv6Address()
                self.source_ipv6_address.parent = self
                self._children_name_map["source_ipv6_address"] = "source-ipv6-address"
                self._children_yang_names.add("source-ipv6-address")
                self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/profiles/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Profiles.Profile, ['profile_name', 'sync_grant_duration', 'general_cos', 'sync_timeout', 'transport', 'announce_timeout', 'cos', 'port_state', 'delay_response_timeout', 'delay_response_grant_duration', 'event_cos', 'dscp', 'general_dscp', 'clock_operation', 'announce_grant_duration', 'unicast_grant_invalid_request', 'event_dscp'], name, value)


            class AnnounceInterval(Entity):
                """
                Announce interval
                
                .. attribute:: time_type
                
                	Interval or Frequency
                	**type**\:  :py:class:`PtpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTime>`
                
                	**default value**\: interval
                
                .. attribute:: time_period
                
                	Time Period
                	**type**\:  :py:class:`PtpTimePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimePeriod>`
                
                	**default value**\: 2
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.AnnounceInterval, self).__init__()

                    self.yang_name = "announce-interval"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_type', YLeaf(YType.enumeration, 'time-type')),
                        ('time_period', YLeaf(YType.enumeration, 'time-period')),
                    ])
                    self.time_type = None
                    self.time_period = None
                    self._segment_path = lambda: "announce-interval"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.AnnounceInterval, ['time_type', 'time_period'], name, value)


            class SourceIpv4Address(Entity):
                """
                Source IPv4 Address
                
                .. attribute:: enable
                
                	Enable source IP address
                	**type**\: bool
                
                .. attribute:: source_ip
                
                	Source IP address to use
                	**type**\: str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.SourceIpv4Address, self).__init__()

                    self.yang_name = "source-ipv4-address"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', YLeaf(YType.boolean, 'enable')),
                        ('source_ip', YLeaf(YType.str, 'source-ip')),
                    ])
                    self.enable = None
                    self.source_ip = None
                    self._segment_path = lambda: "source-ipv4-address"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.SourceIpv4Address, ['enable', 'source_ip'], name, value)


            class Subordinates(Entity):
                """
                Table for subordinate configuration
                
                .. attribute:: subordinate
                
                	Subordinate configuration
                	**type**\: list of  		 :py:class:`Subordinate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Subordinates.Subordinate>`
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Subordinates, self).__init__()

                    self.yang_name = "subordinates"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("subordinate", ("subordinate", Ptp.Profiles.Profile.Subordinates.Subordinate))])
                    self._leafs = OrderedDict()

                    self.subordinate = YList(self)
                    self._segment_path = lambda: "subordinates"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Subordinates, [], name, value)


                class Subordinate(Entity):
                    """
                    Subordinate configuration
                    
                    .. attribute:: transport  (key)
                    
                    	Subordinate Transport Type
                    	**type**\:  :py:class:`PtpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpEncap>`
                    
                    .. attribute:: ethernet
                    
                    	ethernet
                    	**type**\: list of  		 :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Subordinates.Subordinate.Ethernet>`
                    
                    .. attribute:: ipv4_or_ipv6
                    
                    	ipv4 or ipv6
                    	**type**\: list of  		 :py:class:`Ipv4OrIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Subordinates.Subordinate.Ipv4OrIpv6>`
                    
                    

                    """

                    _prefix = 'ptp-cfg'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Profiles.Profile.Subordinates.Subordinate, self).__init__()

                        self.yang_name = "subordinate"
                        self.yang_parent_name = "subordinates"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['transport']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ethernet", ("ethernet", Ptp.Profiles.Profile.Subordinates.Subordinate.Ethernet)), ("ipv4-or-ipv6", ("ipv4_or_ipv6", Ptp.Profiles.Profile.Subordinates.Subordinate.Ipv4OrIpv6))])
                        self._leafs = OrderedDict([
                            ('transport', YLeaf(YType.enumeration, 'transport')),
                        ])
                        self.transport = None

                        self.ethernet = YList(self)
                        self.ipv4_or_ipv6 = YList(self)
                        self._segment_path = lambda: "subordinate" + "[transport='" + str(self.transport) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Profiles.Profile.Subordinates.Subordinate, ['transport'], name, value)


                    class Ethernet(Entity):
                        """
                        ethernet
                        
                        .. attribute:: subordinate_mac_address  (key)
                        
                        	Subordinate MAC Address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Subordinates.Subordinate.Ethernet, self).__init__()

                            self.yang_name = "ethernet"
                            self.yang_parent_name = "subordinate"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['subordinate_mac_address']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('subordinate_mac_address', YLeaf(YType.str, 'subordinate-mac-address')),
                                ('non_negotiated', YLeaf(YType.boolean, 'non-negotiated')),
                            ])
                            self.subordinate_mac_address = None
                            self.non_negotiated = None
                            self._segment_path = lambda: "ethernet" + "[subordinate-mac-address='" + str(self.subordinate_mac_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Subordinates.Subordinate.Ethernet, ['subordinate_mac_address', 'non_negotiated'], name, value)


                    class Ipv4OrIpv6(Entity):
                        """
                        ipv4 or ipv6
                        
                        .. attribute:: subordinate_ip_address  (key)
                        
                        	Subordinate IP Address
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Subordinates.Subordinate.Ipv4OrIpv6, self).__init__()

                            self.yang_name = "ipv4-or-ipv6"
                            self.yang_parent_name = "subordinate"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['subordinate_ip_address']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('subordinate_ip_address', YLeaf(YType.str, 'subordinate-ip-address')),
                                ('non_negotiated', YLeaf(YType.boolean, 'non-negotiated')),
                            ])
                            self.subordinate_ip_address = None
                            self.non_negotiated = None
                            self._segment_path = lambda: "ipv4-or-ipv6" + "[subordinate-ip-address='" + str(self.subordinate_ip_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Subordinates.Subordinate.Ipv4OrIpv6, ['subordinate_ip_address', 'non_negotiated'], name, value)


            class SyncInterval(Entity):
                """
                Sync interval
                
                .. attribute:: time_type
                
                	Interval or Frequency
                	**type**\:  :py:class:`PtpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTime>`
                
                	**default value**\: interval
                
                .. attribute:: time_period
                
                	Time Period
                	**type**\:  :py:class:`PtpTimePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimePeriod>`
                
                	**default value**\: 1
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.SyncInterval, self).__init__()

                    self.yang_name = "sync-interval"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_type', YLeaf(YType.enumeration, 'time-type')),
                        ('time_period', YLeaf(YType.enumeration, 'time-period')),
                    ])
                    self.time_type = None
                    self.time_period = None
                    self._segment_path = lambda: "sync-interval"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.SyncInterval, ['time_type', 'time_period'], name, value)


            class Mains(Entity):
                """
                Table for main configuration
                
                .. attribute:: main
                
                	Main configuration
                	**type**\: list of  		 :py:class:`Main <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Mains.Main>`
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Mains, self).__init__()

                    self.yang_name = "mains"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("main", ("main", Ptp.Profiles.Profile.Mains.Main))])
                    self._leafs = OrderedDict()

                    self.main = YList(self)
                    self._segment_path = lambda: "mains"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Mains, [], name, value)


                class Main(Entity):
                    """
                    Main configuration
                    
                    .. attribute:: transport  (key)
                    
                    	Main Transport Type
                    	**type**\:  :py:class:`PtpEncap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpEncap>`
                    
                    .. attribute:: ethernet
                    
                    	ethernet
                    	**type**\: list of  		 :py:class:`Ethernet <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Mains.Main.Ethernet>`
                    
                    .. attribute:: ipv4_or_ipv6
                    
                    	ipv4 or ipv6
                    	**type**\: list of  		 :py:class:`Ipv4OrIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6>`
                    
                    

                    """

                    _prefix = 'ptp-cfg'
                    _revision = '2017-02-02'

                    def __init__(self):
                        super(Ptp.Profiles.Profile.Mains.Main, self).__init__()

                        self.yang_name = "main"
                        self.yang_parent_name = "mains"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['transport']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("ethernet", ("ethernet", Ptp.Profiles.Profile.Mains.Main.Ethernet)), ("ipv4-or-ipv6", ("ipv4_or_ipv6", Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6))])
                        self._leafs = OrderedDict([
                            ('transport', YLeaf(YType.enumeration, 'transport')),
                        ])
                        self.transport = None

                        self.ethernet = YList(self)
                        self.ipv4_or_ipv6 = YList(self)
                        self._segment_path = lambda: "main" + "[transport='" + str(self.transport) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ptp.Profiles.Profile.Mains.Main, ['transport'], name, value)


                    class Ethernet(Entity):
                        """
                        ethernet
                        
                        .. attribute:: main_mac_address  (key)
                        
                        	Main MAC Address \- only used if Transport is Ethernet
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: delay_asymmetry
                        
                        	The delay asymmetry for this main
                        	**type**\:  :py:class:`DelayAsymmetry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Mains.Main.Ethernet.DelayAsymmetry>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: main_clock_class
                        
                        	Main clock class
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        .. attribute:: priority
                        
                        	Main priority
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: communication
                        
                        	Communication Model
                        	**type**\:  :py:class:`PtpTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTransport>`
                        
                        	**default value**\: unicast
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Mains.Main.Ethernet, self).__init__()

                            self.yang_name = "ethernet"
                            self.yang_parent_name = "main"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['main_mac_address']
                            self._child_container_classes = OrderedDict([("delay-asymmetry", ("delay_asymmetry", Ptp.Profiles.Profile.Mains.Main.Ethernet.DelayAsymmetry))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('main_mac_address', YLeaf(YType.str, 'main-mac-address')),
                                ('main_clock_class', YLeaf(YType.uint32, 'main-clock-class')),
                                ('non_negotiated', YLeaf(YType.boolean, 'non-negotiated')),
                                ('priority', YLeaf(YType.uint32, 'priority')),
                                ('communication', YLeaf(YType.enumeration, 'communication')),
                            ])
                            self.main_mac_address = None
                            self.main_clock_class = None
                            self.non_negotiated = None
                            self.priority = None
                            self.communication = None

                            self.delay_asymmetry = None
                            self._children_name_map["delay_asymmetry"] = "delay-asymmetry"
                            self._children_yang_names.add("delay-asymmetry")
                            self._segment_path = lambda: "ethernet" + "[main-mac-address='" + str(self.main_mac_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Mains.Main.Ethernet, ['main_mac_address', 'main_clock_class', 'non_negotiated', 'priority', 'communication'], name, value)


                        class DelayAsymmetry(Entity):
                            """
                            The delay asymmetry for this main
                            
                            .. attribute:: magnitude
                            
                            	How much longer the main to subordinate path takes than the reverse
                            	**type**\: int
                            
                            	**range:** \-500000000..500000000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: units
                            
                            	The units to use for the delay asymmetry
                            	**type**\:  :py:class:`PtpDelayAsymmetryUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpDelayAsymmetryUnits>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ptp-cfg'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Profiles.Profile.Mains.Main.Ethernet.DelayAsymmetry, self).__init__()

                                self.yang_name = "delay-asymmetry"
                                self.yang_parent_name = "ethernet"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('magnitude', YLeaf(YType.int32, 'magnitude')),
                                    ('units', YLeaf(YType.enumeration, 'units')),
                                ])
                                self.magnitude = None
                                self.units = None
                                self._segment_path = lambda: "delay-asymmetry"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Profiles.Profile.Mains.Main.Ethernet.DelayAsymmetry, ['magnitude', 'units'], name, value)


                    class Ipv4OrIpv6(Entity):
                        """
                        ipv4 or ipv6
                        
                        .. attribute:: main_ip_address  (key)
                        
                        	Main IP Address \- used if Transport is not Ethernet
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: delay_asymmetry
                        
                        	The delay asymmetry for this main
                        	**type**\:  :py:class:`DelayAsymmetry <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6.DelayAsymmetry>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: main_clock_class
                        
                        	Main clock class
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: non_negotiated
                        
                        	Enable non\-negotiated unicast on this interface
                        	**type**\: bool
                        
                        .. attribute:: priority
                        
                        	Main priority
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: communication
                        
                        	Communication Model
                        	**type**\:  :py:class:`PtpTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTransport>`
                        
                        	**default value**\: unicast
                        
                        

                        """

                        _prefix = 'ptp-cfg'
                        _revision = '2017-02-02'

                        def __init__(self):
                            super(Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6, self).__init__()

                            self.yang_name = "ipv4-or-ipv6"
                            self.yang_parent_name = "main"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['main_ip_address']
                            self._child_container_classes = OrderedDict([("delay-asymmetry", ("delay_asymmetry", Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6.DelayAsymmetry))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('main_ip_address', YLeaf(YType.str, 'main-ip-address')),
                                ('main_clock_class', YLeaf(YType.uint32, 'main-clock-class')),
                                ('non_negotiated', YLeaf(YType.boolean, 'non-negotiated')),
                                ('priority', YLeaf(YType.uint32, 'priority')),
                                ('communication', YLeaf(YType.enumeration, 'communication')),
                            ])
                            self.main_ip_address = None
                            self.main_clock_class = None
                            self.non_negotiated = None
                            self.priority = None
                            self.communication = None

                            self.delay_asymmetry = None
                            self._children_name_map["delay_asymmetry"] = "delay-asymmetry"
                            self._children_yang_names.add("delay-asymmetry")
                            self._segment_path = lambda: "ipv4-or-ipv6" + "[main-ip-address='" + str(self.main_ip_address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6, ['main_ip_address', 'main_clock_class', 'non_negotiated', 'priority', 'communication'], name, value)


                        class DelayAsymmetry(Entity):
                            """
                            The delay asymmetry for this main
                            
                            .. attribute:: magnitude
                            
                            	How much longer the main to subordinate path takes than the reverse
                            	**type**\: int
                            
                            	**range:** \-500000000..500000000
                            
                            	**mandatory**\: True
                            
                            .. attribute:: units
                            
                            	The units to use for the delay asymmetry
                            	**type**\:  :py:class:`PtpDelayAsymmetryUnits <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpDelayAsymmetryUnits>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ptp-cfg'
                            _revision = '2017-02-02'

                            def __init__(self):
                                super(Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6.DelayAsymmetry, self).__init__()

                                self.yang_name = "delay-asymmetry"
                                self.yang_parent_name = "ipv4-or-ipv6"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('magnitude', YLeaf(YType.int32, 'magnitude')),
                                    ('units', YLeaf(YType.enumeration, 'units')),
                                ])
                                self.magnitude = None
                                self.units = None
                                self._segment_path = lambda: "delay-asymmetry"

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ptp.Profiles.Profile.Mains.Main.Ipv4OrIpv6.DelayAsymmetry, ['magnitude', 'units'], name, value)


            class Communication(Entity):
                """
                Communication model
                
                .. attribute:: model
                
                	Communication Model
                	**type**\:  :py:class:`PtpTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTransport>`
                
                	**default value**\: unicast
                
                .. attribute:: target_address_set
                
                	Target address set
                	**type**\: bool
                
                	**default value**\: false
                
                .. attribute:: target_address
                
                	Target address
                	**type**\: str
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.Communication, self).__init__()

                    self.yang_name = "communication"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('model', YLeaf(YType.enumeration, 'model')),
                        ('target_address_set', YLeaf(YType.boolean, 'target-address-set')),
                        ('target_address', YLeaf(YType.str, 'target-address')),
                    ])
                    self.model = None
                    self.target_address_set = None
                    self.target_address = None
                    self._segment_path = lambda: "communication"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.Communication, ['model', 'target_address_set', 'target_address'], name, value)


            class DelayRequestMinimumInterval(Entity):
                """
                Minimum delay request interval
                
                .. attribute:: time_type
                
                	Interval or Frequency
                	**type**\:  :py:class:`PtpTime <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTime>`
                
                	**default value**\: interval
                
                .. attribute:: time_period
                
                	Time Period
                	**type**\:  :py:class:`PtpTimePeriod <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_datatypes.PtpTimePeriod>`
                
                	**default value**\: 1
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.DelayRequestMinimumInterval, self).__init__()

                    self.yang_name = "delay-request-minimum-interval"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('time_type', YLeaf(YType.enumeration, 'time-type')),
                        ('time_period', YLeaf(YType.enumeration, 'time-period')),
                    ])
                    self.time_type = None
                    self.time_period = None
                    self._segment_path = lambda: "delay-request-minimum-interval"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.DelayRequestMinimumInterval, ['time_type', 'time_period'], name, value)


            class SourceIpv6Address(Entity):
                """
                Source IPv6 Address
                
                .. attribute:: enable
                
                	Enable source IPv6 address
                	**type**\: bool
                
                .. attribute:: source_ipv6
                
                	Source IPv6 address to use
                	**type**\: str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.Profiles.Profile.SourceIpv6Address, self).__init__()

                    self.yang_name = "source-ipv6-address"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('enable', YLeaf(YType.boolean, 'enable')),
                        ('source_ipv6', YLeaf(YType.str, 'source-ipv6')),
                    ])
                    self.enable = None
                    self.source_ipv6 = None
                    self._segment_path = lambda: "source-ipv6-address"

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.Profiles.Profile.SourceIpv6Address, ['enable', 'source_ipv6'], name, value)


    class UtcOffset(Entity):
        """
        UTC offset configuration
        
        .. attribute:: leap_second_file
        
        	Source file containing leap second information
        	**type**\:  :py:class:`LeapSecondFile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset.LeapSecondFile>`
        
        	**presence node**\: True
        
        .. attribute:: scheduled_offsets
        
        	Table for scheduled UTC offset configuration
        	**type**\:  :py:class:`ScheduledOffsets <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset.ScheduledOffsets>`
        
        .. attribute:: base_offset
        
        	Base UTC offset configuration
        	**type**\: int
        
        	**range:** 0..32767
        
        	**units**\: second
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.UtcOffset, self).__init__()

            self.yang_name = "utc-offset"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("leap-second-file", ("leap_second_file", Ptp.UtcOffset.LeapSecondFile)), ("scheduled-offsets", ("scheduled_offsets", Ptp.UtcOffset.ScheduledOffsets))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('base_offset', YLeaf(YType.uint32, 'base-offset')),
            ])
            self.base_offset = None

            self.leap_second_file = None
            self._children_name_map["leap_second_file"] = "leap-second-file"
            self._children_yang_names.add("leap-second-file")

            self.scheduled_offsets = Ptp.UtcOffset.ScheduledOffsets()
            self.scheduled_offsets.parent = self
            self._children_name_map["scheduled_offsets"] = "scheduled-offsets"
            self._children_yang_names.add("scheduled-offsets")
            self._segment_path = lambda: "utc-offset"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(Ptp.UtcOffset, ['base_offset'], name, value)


        class LeapSecondFile(Entity):
            """
            Source file containing leap second information
            
            .. attribute:: source_url
            
            	URL of source file
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: polling_frequency
            
            	Polling frequency, in days
            	**type**\: int
            
            	**range:** 1..365
            
            	**units**\: day
            
            

            This class is a :ref:`presence class<presence-class>`

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.UtcOffset.LeapSecondFile, self).__init__()

                self.yang_name = "leap-second-file"
                self.yang_parent_name = "utc-offset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self.is_presence_container = True
                self._leafs = OrderedDict([
                    ('source_url', YLeaf(YType.str, 'source-url')),
                    ('polling_frequency', YLeaf(YType.uint32, 'polling-frequency')),
                ])
                self.source_url = None
                self.polling_frequency = None
                self._segment_path = lambda: "leap-second-file"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/utc-offset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffset.LeapSecondFile, ['source_url', 'polling_frequency'], name, value)


        class ScheduledOffsets(Entity):
            """
            Table for scheduled UTC offset configuration
            
            .. attribute:: scheduled_offset
            
            	Scheduled UTC offset configuration
            	**type**\: list of  		 :py:class:`ScheduledOffset <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.UtcOffset.ScheduledOffsets, self).__init__()

                self.yang_name = "scheduled-offsets"
                self.yang_parent_name = "utc-offset"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("scheduled-offset", ("scheduled_offset", Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset))])
                self._leafs = OrderedDict()

                self.scheduled_offset = YList(self)
                self._segment_path = lambda: "scheduled-offsets"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/utc-offset/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.UtcOffset.ScheduledOffsets, [], name, value)


            class ScheduledOffset(Entity):
                """
                Scheduled UTC offset configuration
                
                .. attribute:: date  (key)
                
                	Offset application date, in ISO\-8601 format (YYYY\-MM\-DD)
                	**type**\: str
                
                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                
                .. attribute:: offset
                
                	UTC offset, in seconds
                	**type**\: int
                
                	**range:** 0..32767
                
                	**mandatory**\: True
                
                	**units**\: second
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset, self).__init__()

                    self.yang_name = "scheduled-offset"
                    self.yang_parent_name = "scheduled-offsets"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['date']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('date', YLeaf(YType.str, 'date')),
                        ('offset', YLeaf(YType.uint32, 'offset')),
                    ])
                    self.date = None
                    self.offset = None
                    self._segment_path = lambda: "scheduled-offset" + "[date='" + str(self.date) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/utc-offset/scheduled-offsets/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.UtcOffset.ScheduledOffsets.ScheduledOffset, ['date', 'offset'], name, value)


    class Logging(Entity):
        """
        PTP logging configuration
        
        .. attribute:: best_main_clock
        
        	PTP best main clock logging configuration
        	**type**\:  :py:class:`BestMainClock <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Logging.BestMainClock>`
        
        .. attribute:: servo
        
        	PTP PD Servo logging configuration
        	**type**\:  :py:class:`Servo <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.Logging.Servo>`
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.Logging, self).__init__()

            self.yang_name = "logging"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("best-main-clock", ("best_main_clock", Ptp.Logging.BestMainClock)), ("Cisco-IOS-XR-asr9k-ptp-pd-cfg:servo", ("servo", Ptp.Logging.Servo))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.best_main_clock = Ptp.Logging.BestMainClock()
            self.best_main_clock.parent = self
            self._children_name_map["best_main_clock"] = "best-main-clock"
            self._children_yang_names.add("best-main-clock")

            self.servo = Ptp.Logging.Servo()
            self.servo.parent = self
            self._children_name_map["servo"] = "Cisco-IOS-XR-asr9k-ptp-pd-cfg:servo"
            self._children_yang_names.add("Cisco-IOS-XR-asr9k-ptp-pd-cfg:servo")
            self._segment_path = lambda: "logging"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()


        class BestMainClock(Entity):
            """
            PTP best main clock logging configuration
            
            .. attribute:: changes
            
            	Enable best main clock changes logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.Logging.BestMainClock, self).__init__()

                self.yang_name = "best-main-clock"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('changes', YLeaf(YType.empty, 'changes')),
                ])
                self.changes = None
                self._segment_path = lambda: "best-main-clock"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/logging/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Logging.BestMainClock, ['changes'], name, value)


        class Servo(Entity):
            """
            PTP PD Servo logging configuration
            
            .. attribute:: events
            
            	Enable servo events logging
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            

            """

            _prefix = 'asr9k-ptp-pd-cfg'
            _revision = '2017-05-20'

            def __init__(self):
                super(Ptp.Logging.Servo, self).__init__()

                self.yang_name = "servo"
                self.yang_parent_name = "logging"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('events', YLeaf(YType.empty, 'events')),
                ])
                self.events = None
                self._segment_path = lambda: "Cisco-IOS-XR-asr9k-ptp-pd-cfg:servo"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/logging/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.Logging.Servo, ['events'], name, value)


    class TransparentClock(Entity):
        """
        Transparent clock configuration
        
        .. attribute:: domains
        
        	Table of domains containing transparent clock configuration
        	**type**\:  :py:class:`Domains <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.TransparentClock.Domains>`
        
        

        """

        _prefix = 'ptp-cfg'
        _revision = '2017-02-02'

        def __init__(self):
            super(Ptp.TransparentClock, self).__init__()

            self.yang_name = "transparent-clock"
            self.yang_parent_name = "ptp"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("domains", ("domains", Ptp.TransparentClock.Domains))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict()

            self.domains = Ptp.TransparentClock.Domains()
            self.domains.parent = self
            self._children_name_map["domains"] = "domains"
            self._children_yang_names.add("domains")
            self._segment_path = lambda: "transparent-clock"
            self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/%s" % self._segment_path()


        class Domains(Entity):
            """
            Table of domains containing transparent clock
            configuration
            
            .. attribute:: domain
            
            	Transparent clock domain configuration
            	**type**\: list of  		 :py:class:`Domain <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ptp_cfg.Ptp.TransparentClock.Domains.Domain>`
            
            

            """

            _prefix = 'ptp-cfg'
            _revision = '2017-02-02'

            def __init__(self):
                super(Ptp.TransparentClock.Domains, self).__init__()

                self.yang_name = "domains"
                self.yang_parent_name = "transparent-clock"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("domain", ("domain", Ptp.TransparentClock.Domains.Domain))])
                self._leafs = OrderedDict()

                self.domain = YList(self)
                self._segment_path = lambda: "domains"
                self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/transparent-clock/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(Ptp.TransparentClock.Domains, [], name, value)


            class Domain(Entity):
                """
                Transparent clock domain configuration
                
                .. attribute:: domain  (key)
                
                	Domain
                	**type**\: str
                
                	**pattern:** (all)
                
                

                """

                _prefix = 'ptp-cfg'
                _revision = '2017-02-02'

                def __init__(self):
                    super(Ptp.TransparentClock.Domains.Domain, self).__init__()

                    self.yang_name = "domain"
                    self.yang_parent_name = "domains"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['domain']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('domain', YLeaf(YType.str, 'domain')),
                    ])
                    self.domain = None
                    self._segment_path = lambda: "domain" + "[domain='" + str(self.domain) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-ptp-cfg:ptp/transparent-clock/domains/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(Ptp.TransparentClock.Domains.Domain, ['domain'], name, value)

    def clone_ptr(self):
        self._top_entity = Ptp()
        return self._top_entity

