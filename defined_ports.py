# Copyright 2016, Manito Networks, LLC. All rights reserved

# Array of protocol names and numbers according to: 
# IANA http://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.xhtml 
# Wikipedia https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers
# :{"Name": ""}
registered_ports = {
0:{"Name": "Reserved"},
1:{"Name": "TCP Port Service Multiplexer"},
2:{"Name": "Management Utility"},
3:{"Name": "Compression Process"},
5:{"Name": "Remote Job Entry"},
7:{"Name": "Echo"},
9:{"Name": "Discard"},
11:{"Name": "Active Users"},
13:{"Name": "Daytime"},
17:{"Name": "Quote of the Day"},
18:{"Name": "Message Send Protocol"},
19:{"Name": "Character Generator"},
20:{"Name": "FTP Data","Category":"File Transfer"},
21:{"Name": "FTP Control","Category":"File Transfer"},
22:{"Name": "SSH","Category":"Remote Administration"},
23:{"Name": "Telnet","Category":"Remote Administration"},
24:{"Name": "Private Mail System"},
25:{"Name": "SMTP","Category":"Email"},
27:{"Name": "NSW User System FE"},
29:{"Name": "MSG ICP"},
31:{"Name": "MSG Authentication"},
33:{"Name": "Display Support Protocol"},
35:{"Name": "Printer Server"},
37:{"Name": "Time"},
38:{"Name": "Route Access Protocol"},
39:{"Name": "Resource Location Protocol"},
41:{"Name": "Graphics"},
42:{"Name": "WINS","Category":"Name Resolution"},
43:{"Name": "WHOIS"},
44:{"Name": "MPM FLAGS Protocol"},
45:{"Name": "Message Processing Module [recv]"},
46:{"Name": "MPM [default send]"},
47:{"Name": "NI FTP"},
48:{"Name": "Digital Audit Daemon"},
49:{"Name": "TACACS+","Category":"Remote Administration"},
50:{"Name": "ESP"},
52:{"Name": "XNS Time Protocol"},
53:{"Name": "DNS","Category":"Name Resolution"},
54:{"Name": "XNS Clearinghouse"},
55:{"Name": "ISI Graphics Language"},
56:{"Name": "XNS Authentication"},
57:{"Name": "any private terminal access"},
58:{"Name": "XNS Mail"},
59:{"Name": "any private file service"},
61:{"Name": "NI MAIL"},
62:{"Name": "ACA Services"},
63:{"Name": "WHOIS++"},
64:{"Name": "Communications Integrator"},
65:{"Name": "TACACS-Database Service"},
66:{"Name": "Oracle SQL*NET"},
67:{"Name": "BOOTP Server / DHCP"},
68:{"Name": "BOOTP Client / DHCP"},
69:{"Name": "TFTP","Category":"File Transfer"},
70:{"Name": "Gopher"},
71:{"Name": "Remote Job Service"},
72:{"Name": "Remote Job Service"},
73:{"Name": "Remote Job Service"},
74:{"Name": "Remote Job Service"},
75:{"Name": "any private dial out service"},
76:{"Name": "Distributed External Object Store"},
77:{"Name": "RJE Service"},
78:{"Name": "vettcp"},
79:{"Name": "Finger"},
80:{"Name": "HTTP","Category":"Web"},
81:{"Name": "Torpark Onion Routing"},
82:{"Name": "Torpark Control"},
83:{"Name": "MIT ML Device"},
84:{"Name": "Common Trace Facility"},
85:{"Name": "MIT ML Device"},
86:{"Name": "Micro Focus Cobol"},
87:{"Name": "Private Terminal Link"},
88:{"Name": "Kerberos","Category":"AAA"},
89:{"Name": "SU/MIT Telnet Gateway"},
90:{"Name": "DNSIX Securit Attribute Token Map"},
91:{"Name": "MIT Dover Spooler"},
92:{"Name": "Network Printing Protocol","Category":"Printing"},
93:{"Name": "Device Control Protocol"},
#94:'Tivoli Object Dispatcher',
#95:'SUPDUP',
#96:'DIXIE Protocol Specification',
#97:'Swift Remote Virtural File Protocol',
#98:'TAC News',
#99:'Metagram Relay',
#101:'NIC Host Name Server',
#102:'ISO-TSAP Class 0',
#103:'Genesis Point-to-Point Trans Net',
#104:'ACR-NEMA Digital Imag. & Comm. 300',
#105:'CCSO name server protocol',
#106:'3COM-TSMUX',
107:{"Name": "Remote Telnet Service"},
#108:'SNA Gateway Access Server',
109:{"Name": "POP2","Category":"Email"},
110:{"Name": "POP3","Category":"Email"},
111:{"Name": "Portmapper, Sun RPC"},
#112:'McIDAS Data Transmission Protocol',
115:{"Name": "Simple FTP","Category":"File Transfer"},
#116:'ANSA REX Notify',
#117:'UUCP Path Service',
118:{"Name": "SQL Services","Category":"Databases"},
119:{"Name": "NNTP"},
#120:'CFDPTKT',
#121:'Encore Expedited Remote Pro.Call',
#122:'SMAKYNET',
123:{"Name": "NTP","Category":"Time"},
#124:'ANSA REX Trader',
#125:'Locus PC-Interface Net Map Ser',
#126:'NXEdit',
#127:'Locus PC-Interface Conn Server',
#128:'GSS X License Verification',
#129:'Password Generator Protocol',
130:{"Name": "Cisco FNATIVE"},
131:{"Name": "Cisco TNATIVE"},
132:{"Name": "Cisco SYSMAINT"},
#133:'Statistics Service',
#134:'INGRES-NET Service',
#135:'DCE endpoint resolution',
#136:'PROFILE Naming System',
137:{"Name": "NETBIOS Name Service","Category":"Name Resolution"},
138:{"Name": "NETBIOS Datagram Service"},
139:{"Name": "NETBIOS Session Service"},
#140:'EMFIS Data Service',
#141:'EMFIS Control Service',
#142:'Britton-Lee IDM',
143:{"Name": "IMAP","Category":"Email"},
#144:'Universal Management Architecture',
#145:'UAAC Protocol',
#146:'ISO-IP0',
#147:'ISO-IP',
#148:'Jargon',
#149:'AED 512 Emulation Service',
150:{"Name": "SQL-NET"},
#151:'HEMS',
#152:'Background File Transfer Program',
153:{"Name": "SGMP"},
#154:'NETSC',
#155:'NETSC',
156:{"Name": "SQL Service"},
#157:'KNET/VM Command/Message Protocol',
#158:'PCMail Server',
#159:'NSS-Routing',
160:{"Name": "SGMP-TRAPS"},
161:{"Name": "SNMP","Category":"Remote Administration"},
162:{"Name": "SNMP Trap","Category":"Remote Administration"},
#163:'CMIP/TCP Manager',
#164:'CMIP/TCP Agent',
#165:'Xerox',
#166:'Sirius Systems',
#167:'NAMP',
168:{"Name": "RSVD"},
#169:'SEND',
170:{"Name": "Network PostScript","Category":"Printing"},
#171:'Network Innovations Multiplex',
#172:'Network Innovations CL/1',
#173:'Xyplex',
#174:'MAILQ',
#175:'VMNET',
#176:'GENRAD-MUX',
177:{"Name": "X Display Manager Control Protocol"},
#178:'NextStep Window Server',
179:{"Name": "BGP","Category":"Routing"},
#180:'Intergraph',
#181:'Unify',
#182:'Unisys Audit SITP',
#183:'OCBinder',
#184:'OCServer',
#185:'Remote-KIS',
#186:'KIS Protocol',
#187:'Application Communication Interface',
#188:'Plus Five\'s MUMPS',
#189:'Queued File Transport',
#190:'Gateway Access Control Protocol',
#191:'Prospero Directory Service',
#192:'OSU Network Monitoring System',
#193:'Spider Remote Monitoring Protocol',
194:{"Name": "IRC","Category":"Chat"},
#195:'DNSIX Network Level Module Audit',
#196:'DNSIX Session Mgt Module Audit Redir',
197:{"Name": "Directory Location Service"},
198:{"Name": "Directory Location Service Monitor"},
#199:'SMUX',
#200:'IBM System Resource Controller',
201:{"Name": "AppleTalk Routing Maintenance","Category":"Apple"},
202:{"Name": "AppleTalk Name Binding","Category":"Apple"},
203:{"Name": "AppleTalk Unused","Category":"Apple"},
204:{"Name": "AppleTalk Echo","Category":"Apple"},
205:{"Name": "AppleTalk Unused","Category":"Apple"},
206:{"Name": "AppleTalk Zone Information","Category":"Apple"},
207:{"Name": "AppleTalk Unused","Category":"Apple"},
208:{"Name": "AppleTalk Unused","Category":"Apple"},
#209:'The Quick Mail Transfer Protocol',
#210:'ANSI Z39.50',
#211:'Texas Instruments 914C/G Terminal',
#212:'ATEXSSTR',
213:{"Name": "IPX","Category":"Novell"},
#214:'VM PWSCS',
#215:'Insignia Solutions',
#216:'Computer Associates Int\'l License Server',
#217:'dBASE Unix',
#218:'Netix Message Posting Protocol',
#219:'Unisys ARPs',
220:{"Name": "IMAP3","Category":"Email"},
#221:'Berkeley rlogind with SPX auth',
#222:'Berkeley rshd with SPX auth',
223:{"Name": "Certificate Distribution Center","Category":"AAA"},
#224:'masqdialer',
#242:'Direct',
#243:'Survey Measurement',
#244:'inbusiness',
#245:'LINK',
#246:'Display Systems Protocol',
#247:'SUBNTBCST_TFTP',
#248:'bhfhs',
#256:'RAP',
#257:'Secure Electronic Transaction',
#259:'Efficient Short Remote Operations',
#260:'Openport',
#261:'IIOP Name Service over TLS/SSL',
#262:'Arcisdms',
#263:'HDAP',
264:{"Name": "BGMP"},
#265:'X-Bone CTL',
#266:'SCSI on ST',
#267:'Tobit David Service Layer',
#268:'Tobit David Replica',
#269:'MANET Protocols',
#270:'Q-mode encapsulation for GIST messages',
#271:'IETF NEA PT-TLS',
#280:'http-mgmt',
#281:'Personal Link',
#282:'Cable Port A/X',
#283:'rescap',
#284:'corerjd',
#286:'FXP Communication',
#287:'K-BLOCK',
#308:'Novastor Backup',
#309:'EntrustTime',
#310:'bhmds',
#311:'AppleShare IP WebAdmin',
312:{"Name": "VSLMP"},
#313:'Magenta Logic',
#314:'Opalis Robot',
#315:'DPSI',
#316:'decAuth',
#317:'Zannet',
318:{"Name": "PKIX TimeStamp"},
#319:'PTP Event',
#320:'PTP General',
321:{"Name": "PIP"},
322:{"Name": "RTSPS"},
#323:'Resource PKI to Router Protocol',
#324:'Resource PKI to Router Protocol over TLS',
#333:'Texar Security Port',
#344:'Prospero Data Access Protocol',
#345:'Perf Analysis Workbench',
#346:'Zebra server',
#347:'Fatmen Server',
348:{"Name": "Cabletron Management Protocol"},
#349:'mftp',
#350:'MATIP Type A',
#351:'MATIP Type B',
#352:'DTAG',
#353:'NDSAUTH',
#354:'bh611',
#355:'DATEX-ASN',
#356:'Cloanto Net 1',
#357:'bhevent',
#358:'Shrinkwrap',
#359:'Network Security Risk Management Protocol',
#360:'scoi2odialog',
#361:'Semantix',
#362:'SRS Send',
363:{"Name": "RSVP Tunnel"},
#364:'Aurora CMGR',
#365:'DTK',
#366:'ODMR',
#367:'MortgageWare',
#368:'QbikGDP',
#369:'rpc2portmap',
#370:'codaauth2',
#371:'Clearcase',
#372:'ListProcessor',
#373:'Legent Corporation',
#374:'Legent Corporation',
#375:'Hassle',
#376:'Amiga Envoy Network Inquiry Proto',
#377:'NEC Corporation',
#378:'NEC Corporation',
#379:'TIA/EIA/IS-99 modem client',
#380:'TIA/EIA/IS-99 modem server',
#381:'HP performance data collector',
#382:'HP performance data managed node',
#383:'HP performance data alarm manager',
#384:'A Remote Network Server System',
#385:'IBM Application',
#386:'ASA Message Router Object Def.',
#387:'Appletalk Update-Based Routing Pro.',
#388:'Unidata LDM',
389:{"Name": "LDAP","Category":"AAA"},
#390:'UIS',
#391:'SynOptics SNMP Relay Port',
#392:'SynOptics Port Broker Port',
#393:'Meta5',
#394:'EMBL Nucleic Data Transfer',
#395:'NetScout Control Protocol',
396:{"Name":"Novell Netware over IP","Category":"Novell"},
#397:'Multi Protocol Trans. Net.',
#398:'Kryptolan',
#399:'ISO Transport Class 2 Non-Control over TCP',
#400:'Oracle Secure Backup',
401:{"Name":"Uninterruptible Power Supply"},
#402:'Genie Protocol',
#403:'decap',
#404:'nced',
#405:'ncld',
#406:'Interactive Mail Support Protocol',
#407:'Timbuktu',
#408:'Prospero Resource Manager Sys. Man.',
#409:'Prospero Resource Manager Node Man.',
#410:'DECLadebug Remote Debug Protocol',
#411:'Remote MT Protocol',
#412:'Trap Convention Port',
#413:'Storage Management Services Protocol',
#414:'InfoSeek',
#415:'BNet',
#416:'Silverplatter',
#417:'Onmux',
#418:'Hyper-G',
#419:'Ariel 1',
#420:'SMPTE',
#421:'Ariel 2',
#422:'Ariel 3',
#423:'IBM Operations Planning and Control Start',
#424:'IBM Operations Planning and Control Track',
#425:'ICAD',
#426:'smartsdp',
427:{"Name":"SLP"},
#428:'OCS_CMU',
#429:'OCS_AMU',
#430:'UTMPSD',
#431:'UTMPCD',
#432:'IASD',
#433:'NNSP',
#434:'MobileIP-Agent',
#435:'MobilIP-MN',
#436:'DNA-CML',
#437:'comscm',
#438:'dsfgw',
#439:'dasp',
#440:'sgcp',
#441:'decvms-sysmgt',
#442:'cvc_hostd',
443:{"Name":"HTTPS","Category":"Web"},
444:{"Name":"SNPP"},
445:{"Name":"Microsoft-DS","Category":"File Transfer"},
#446:'DDM-Remote Relational Database Access',
#447:'DDM-Distributed File Management',
#448:'DDM-Remote DB Access Using Secure Sockets',
#449:'AS Server Mapper',
#450:'Computer Supported Telecomunication Applications',
#451:'Cray Network Semaphore server',
#452:'Cray SFS config server',
#453:'CreativeServer',
#454:'ContentServer',
#455:'CreativePartnr',
#456:'macon-tcp',
#457:'scohelp',
458:{"Name":"Apple QuickTime","Category":"Apple"},
#459:'ampr-rcmd',
#460:'skronk',
#461:'DataRampSrv',
#462:'DataRampSrvSec',
#463:'alpes',
#464:'kpasswd',
#465:'URL Rendesvous Directory for SSM',
#466:'digital-vrc',
#467:'mylex-mapd',
#468:'proturis',
#469:'Radio Control Protocol',
#470:'scx-proxy',
#471:'Mondex',
#472:'ljk-login',
#473:'hybrid-pop',
#474:'tn-tl-w1',
#475:'tcpnethaspsrv',
#476:'tn-tl-fd1',
#477:'ss7ns',
#478:'spsc',
#479:'iafserver',
#480:'iafdbase',
#481:'Ph service',
#482:'bgs-nsi',
#483:'ulpnet',
#484:'Integra Software Management Environment',
#485:'Air Soft Power Burst',
#486:'avian',
#487:'saft Simple Asynchronous File Transfer',
#488:'gss-http',
#489:'nest-protocol',
#490:'micom-pfs',
#491:'go-login',
#492:'Transport Independent Convergence for FNA',
#493:'Transport Independent Convergence for FNA',
494:{"Name":"POV-Ray"},
#495:'intecourier',
#496:'PIM-RP-DISC',
#497:'Retrospect backup and restore service',
#498:'siam',
#499:'ISO ILL Protocol',
500:{"Name":"ISAKMP"},
#501:'STMF',
#502:'Modbus Application Protocol',
#503:'Intrinsa',
#504:'citadel',
#505:'mailbox-lm',
#506:'ohimsrv',
#507:'crs',
#508:'xvttp',
#509:'snare',
#510:'FirstClass Protocol',
#511:'PassGo',
512:{"Name":"Remote Process Execution"},
513:{"Name":"Rlogin","Category":"Remote Administration"},
514:{"Name":"Syslog","Category":"Remote Administration"},
515:{"Name": "LPD","Category":"Printing"},
#516:'videotex',
#517:'Tenex Link-Like',
#518:'Ntalk',
#519:'unixtime',
520:{"Name":"RIP","Category":"Routing"},
521:{"Name":"RIPng","Category":"Routing"},
#522:'ULP',
523:{"Name":"IBM-DB2"},
524:{"Name":"NCP"},
#525:'timeserver',
#526:'newdate',
#527:'Stock IXChange',
#528:'Customer IXChange',
529:{"Name":"IRC-SERV"},
530:{"Name":"RPC"},
#531:'chat',
#532:'readnews',
#533:'for emergency broadcasts',
#534:'windream Admin',
#535:'iiop',
#536:'opalis-rdv',
537:{"Name":"Networked Media Streaming Protocol"},
#538:'gdomap',
#539:'Apertus Technologies Load Determination',
#540:'uucpd',
#541:'uucp-rlogin',
#542:'commerce',
#544:'krcmd',
#545:'appleqtcsrvr',
546:{"Name":"DHCPv6 Client"},
547:{"Name":"DHCPv6 Server"},
548:{"Name":"AFP over TCP"},
#549:'IDFP',
#550:'new-who',
#551:'cybercash',
#552:'DeviceShare',
#553:'pirp',
554:{"Name":"RTSP"},
556:{"Name":"RFS Server"},
#557:'openvms-sysipc',
#558:'SDNSKMP',
#559:'TEEDTAP',
#560:'rmonitord',
#562:'chcmd',
563:{"Name":"NNTP over TLS/SSL"},
#564:'plan 9 file service',
565:{"Name":"WHOAMI"},
#566:'streettalk',
#567:'banyan-rpc',
#568:'microsoft shuttle',
#569:'microsoft rome',
#570:'demon',
#571:'udemon',
#572:'sonar',
#573:'banyan-vip',
#574:'FTP Software Agent System',
#575:'VEMMI',
#576:'ipcd',
#577:'vnas',
#578:'ipdd',
#579:'decbsrv',
#580:'SNTP HEARTBEAT',
#581:'Bundle Discovery Protocol',
#582:'SCC Security',
#583:'Philips Video-Conferencing',
584:{"Name":"Key Server","Category":"AAA"},
#585:'De-registered',
#586:'Password Change',
587:{"Name":"SMTP Submission","Category":"Email"},
#588:'CAL',
#589:'EyeLink',
#590:'TNS CML',
591:{"Name":"FileMaker HTTP Alternate"},
#592:'Eudora Set',
#593:'HTTP RPC Ep Map',
#594:'TPIP',
#595:'CAB Protocol',
#596:'SMSD',
#597:'PTC Name Service',
#598:'SCO Web Server Manager 3',
#599:'Aeolon Core Protocol',
600:{"Name":"Sun IPC Server"},
#601:'Reliable Syslog Service',
#602:'XML-RPC over BEEP',
603:{"Name": "IDXP"},
#604:'TUNNEL',
#605:'SOAP over BEEP',
#606:'Cray Unified Resource Manager',
#607:'nqs',
#608:'Sender-Initiated/Unsolicited File Transfer',
#609:'npmp-trap',
#610:'npmp-local',
#611:'npmp-gui',
#612:'HMMP Indication',
#613:'HMMP Operation',
#614:'SSLshell',
#615:'Internet Configuration Manager',
#616:'SCO System Administration Server',
#617:'SCO Desktop Administration Server',
#618:'DEI-ICDA',
#619:'Compaq EVM',
#620:'SCO WebServer Manager',
#621:'ESCP',
#622:'Collaborator',
#623:'DMTF OOB Web Services Management Protocol',
#624:'Crypto Admin',
#625:'DEC DLM',
#626:'ASIA',
#627:'PassGo Tivoli',
#628:'QMQP',
#629:'3Com AMP3',
#630:'RDA',
#631:'IPP',
#632:'bmpp',
#633:'Service Status Update (Sterling Software)',
#634:'ginad',
#635:'RLZ DBase',
636:{"Name": "LDAP over TLS/SSL"},
#637:'lanserver',
#638:'mcns-sec',
639:{"Name": "MSDP"},
#640:'entrust-sps',
#641:'repcmd',
#642:'ESRO-EMSDP V1.3',
#643:'SANity',
#644:'dwr',
#645:'PSSC',
646:{"Name": "LDP"},
647:{"Name": "DHCP Failover"},
#648:'Registry Registrar Protocol (RRP)',
#649:'Cadview-3d',
#650:'OBEX',
#651:'IEEE MMS',
#652:'HELLO_PORT',
#653:'RepCmd',
#654:'AODV',
#655:'TINC',
#656:'SPMP',
#657:'RMC',
#658:'TenFold',
#660:'MacOS Server Admin',
#661:'HAP',
662:{"Name": "PFTP"},
#663:'PureNoise',
#664:'DMTF out-of-band secure web services management protocol',
#665:'Sun DR',
#666:'Doom',
#667:'campaign contribution disclosures - SDR Technologies',
#668:'MeComm',
#669:'MeRegister',
#670:'VACDSM-SWS',
#671:'VACDSM-APP',
#672:'VPPS-QUA',
#673:'CIMPLEX',
#674:'ACAP',
#675:'DCTP',
#676:'VPPS Via',
#677:'Virtual Presence Protocol',
#678:'GNU Generation Foundation NCP',
#679:'MRM',
#680:'entrust-aaas',
#681:'entrust-aams',
#682:'XFR',
#683:'CORBA IIOP',
#684:'CORBA IIOP SSL',
#685:'MDC Port Mapper',
#686:'Hardware Control Protocol Wismar',
#687:'asipregistry',
#688:'ApplianceWare managment protocol',
#689:'NMAP',
#690:'Velneo Application Transfer Protocol',
691:{"Name": "MS Exchange Routing"},
#692:'Hyperwave-ISP',
#693:'almanid Connection Endpoint',
#694:'ha-cluster',
#695:'IEEE-MMS-SSL',
#696:'RUSHD',
#697:'UUIDGEN',
#698:'OLSR',
#699:'Access Network',
#700:'Extensible Provisioning Protocol',
#701:'Link Management Protocol (LMP)',
#702:'IRIS over BEEP',
#704:'errlog copy/server daemon',
#705:'AgentX',
#706:'SILC',
#707:'Borland DSJ',
#709:'Entrust Key Management Service Handler',
#710:'Entrust Administration Service Handler',
711:{"Name": "Cisco TDP"},
#712:'TBRPF',
#713:'IRIS over XPC',
#714:'IRIS over XPCS',
#715:'IRIS-LWZ',
#716:'PANA Messages',
#729:'IBM NetView DM/6000 Server/Client',
#730:'IBM NetView DM/6000 send/tcp',
#731:'IBM NetView DM/6000 receive/tcp',
#741:'netGW',
#742:'Network based Rev. Cont. Sys.',
#744:'Flexible License Manager',
#747:'Fujitsu Device Control',
#748:'Russell Info Sci Calendar Manager',
749:{"Name": "Kerberos Administration","Category":"AAA"},
750:{"Name": "Kerberos v4","Category":"AAA"},
#754:'Send',
#767:'Phone',
#774:'ACMAINT_DBD',
#775:'ACMAINT_TRANSD',
#777:'Multiling HTTP',
#800:'MDBS_Daemon Replacement',
#802:'Modbus Application Protocol Secure',
#810:'FCP',
#828:'itm-mcell-s',
#829:'PKIX-3 CA/RA',
#830:'NETCONF over SSH',
#831:'NETCONF over BEEP',
#832:'NETCONF for SOAP over HTTPS',
#833:'NETCONF for SOAP over BEEP',
843:{"Name": "Adobe Flash"},
847:{"Name": "DHCP Failover 2"},
#848:'GDOI',
853:{"Name": "DNS over TLS/DTLS","Category":"Name Resolution"},
860:{"Name": "iSCSI","Category":"Storage"},
#861:'OWAMP-Control',
#862:'Two-way Active Measurement Protocol (TWAMP) Control',
873:{"Name": "RSYNC","Category":"File Transfer"},
#886:'ICL coNETion locate server',
#887:'ICL coNETion server info',
#888:'AccessBuilder',
#900:'OMG Initial Refs',
#901:'SMPNAMERES',
#902:'Self Documenting Telnet Door',
#903:'Self Documenting Telnet Panic Door',
#910:'Kerberized Internet Negotiation of Keys (KINK)',
#911:'xact-backup',
#912:'APEX relay-relay service',
#913:'APEX endpoint-relay service',
989:{"Name": "FTPS Data","Category":"File Transfer"},
990:{"Name": "FTPS Control","Category":"File Transfer"},
#991:'Netnews Administration System',
992:{"Name": "Telnet over TLS/SSL","Category":"Remote Administration"},
993:{"Name": "IMAP4 over TLS/SSL","Category":"Email"},
995:{"Name": "POP3 over TLS/SSL","Category":"Email"},
#996:'vsinet',
#999:'Applix ac',
1008:{"Name": "Sun Solaris"},
#1010:'Surf',
#1021:'RFC3692-style Experiment 1',
#1022:'RFC3692-style Experiment 2'
}


# Non-registered, but commonly defined ports
other_ports = {
1027:{"Name": "IPv6 6a44","Category":"IPv6"},
1029:{"Name": "Microsoft DCOM"},
1071:{"Name": "L2TP","Category":"VPN"},
1080:{"Name": "SOCKS Proxy"},
1194:{"Name": "OpenVPN","Category":"VPN"},
1241:{"Name": "Nessus"},
1433:{"Name": "Microsoft SQL Server","Category":"Databases"},
1434:{"Name": "Microsoft SQL Monitor","Category":"Databases"},
1512:{"Name": "WINS","Category":"Name Resolution"},
1723:{"Name": "PPTP","Category":"VPN"},
1725:{"Name": "Steam","Category":"Games"},
1812:{"Name": "RADIUS","Category":"AAA"},
1813:{"Name": "RADIUS","Category":"AAA"},
1900:{"Name": "UPnP","Category":"UPnP"},
2049:{"Name": "NFS","Category":"Storage"},
2055:{"Name": "Netflow","Category":"Remote Administrationistration"},
3000:{"Name": "BitTorrent Sync","Category":"P2P"},
3306:{"Name": "MySQL","Category":"Databases"},
3074:{"Name": "XBOX Live","Category":"Games"},
3225:{"Name": "FCIP"},
3389:{"Name": "RDP","Category":"Remote Administrationistration"},
3390:{"Name": "Alternate RDP","Category":"Remote Administrationistration"},
3478:{"Name": "Playstation","Category":"Games"},
3479:{"Name": "Playstation","Category":"Games"},
3480:{"Name": "Playstation","Category":"Games"},
3544:{"Name": "Teredo","Category":"IPv6"},
3658:{"Name": "Playstation","Category":"Games"},
3784:{"Name": "BFD (RFC 5881)"},
4443:{"Name": "Alternate HTTPS","Category":"Web"},
4500:{"Name": "IPSEC NAT Traversal","Category":"VPN"},
4569:{"Name": "Asterisk PBX"},
5000:{"Name": "UPnP","Category":"UPnP"},
5004:{"Name": "RTP","Category":"Streaming Media"},
5005:{"Name": "RTP","Category":"Streaming Media"},
5060:{"Name": "SIP","Category":"SIP"},
5061:{"Name": "SIP (TLS)","Category":"SIP"},
5062:{"Name": "Incoming SIP","Category":"SIP"},
5063:{"Name": "SIP Requests for AV Conferencing","Category":"SIP"},
5223:{"Name": "Push Notifications","Category":"Apple"},
5228:{"Name": "Google Services"},
5432:{"Name": "PostgreSQL","Category":"Databases"},
5678:{"Name": "Mikrotik NDP","Category":"Mikrotik"},
5900:{"Name": "VNC","Category":"Remote Administrationistration"},
5901:{"Name": "VNC1","Category":"Remote Administrationistration"},
5902:{"Name": "VNC2","Category":"Remote Administrationistration"},
5903:{"Name": "VNC3","Category":"Remote Administrationistration"},
6881:{"Name": "BitTorrent","Category":"P2P"},
6882:{"Name": "BitTorrent","Category":"P2P"},
6883:{"Name": "BitTorrent","Category":"P2P"},
6884:{"Name": "BitTorrent","Category":"P2P"},
6885:{"Name": "BitTorrent","Category":"P2P"},
6886:{"Name": "BitTorrent","Category":"P2P"},
6887:{"Name": "BitTorrent","Category":"P2P"},
6888:{"Name": "BitTorrent","Category":"P2P"},
6889:{"Name": "BitTorrent","Category":"P2P"},
8057:{"Name": "Persistent Shared Object Model Connections"},
8058:{"Name": "Persistent Shared Object Model Connections"},
8080:{"Name": "HTTP Proxy","Category":"Web"},
8291:{"Name": "Mikrotik Winbox","Category":"Mikrotik"},
8333:{"Name": "Bitcoin","Category":"Crypto Currency"},
8728:{"Name": "Mikrotik API","Category":"Mikrotik"},
8729:{"Name": "Mikrotik API SSL","Category":"Mikrotik"},
8777:{"Name": "Misc. Games","Category":"Games"},
9293:{"Name": "Playstation Remote Play","Category":"Games"},
10001:{"Name": "Ubiquiti Discovery Protocol","Category":"Remote Administrationistration"}
}