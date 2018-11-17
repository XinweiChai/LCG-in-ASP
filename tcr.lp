% This file was generated from the PH model 'tcrsig40_flat.ph'

% Processes
process("AP1", 0..1).
process("CD45", 0..1).
process("CD45LCKTCRbind", 0..7).
process("CD8", 0..1).
process("CRE", 0..1).
process("CREB", 0..1).
process("Ca", 0..1).
process("Calcin", 0..1).
process("DAG", 0..1).
process("DAGPKCth", 0..3).
process("ERK", 0..1).
process("Fos", 0..1).
process("FosJun", 0..3).
process("Fyn", 0..1).
process("FynLCKTCRbind", 0..7).
process("Gads", 0..1).
process("Grb2Sos", 0..1).
process("Grb2SosRasGRP1", 0..3).
process("IKK", 0..1).
process("IP3", 0..1).
process("IkB", 0..1).
process("Itk", 0..1).
process("ItkRlk", 0..3).
process("JNK", 0..1).
process("Jun", 0..1).
process("LAT", 0..1).
process("LCK", 0..1).
process("LCKTCRbind", 0..3).
process("MEK", 0..1).
process("NFAT", 0..1).
process("NFkB", 0..1).
process("PAGCsk", 0..1).
process("PAGCskCD8CD45", 0..7).
process("PKCth", 0..1).
process("PLCg_a", 0..1).
process("PLCg_b", 0..1).
process("Raf", 0..1).
process("Ras", 0..1).
process("RasGRP1", 0..1).
process("Rlk", 0..1).
process("Rsk", 0..1).
process("SEK", 0..1).
process("Slp76", 0..1).
process("TCRbind", 0..1).
process("TCRbindFyn", 0..3).
process("TCRlig", 0..1).
process("TCRphos", 0..1).
process("ZAP70", 0..1).
process("ZAP70Slp76", 0..3).
process("ZAP70Slp76PLCg_b", 0..7).
process("__coop0", 0..3).
process("cCbl", 0..1).
process("cCblTCRlig", 0..3).
process("cCblTCRphosLCK", 0..7).

% Actions
action("CD45",0,"CD45LCKTCRbind",7,3).
action("LCK",0,"CD45LCKTCRbind",7,5).
action("TCRbind",0,"CD45LCKTCRbind",7,6).
action("cCbl",1,"cCblTCRlig",0,2).
action("TCRlig",1,"cCblTCRlig",0,1).
action("MEK",1,"ERK",0,1).
action("ZAP70",1,"ZAP70Slp76PLCg_b",3,7).
action("Slp76",0,"ZAP70Slp76PLCg_b",3,1).
action("PLCg_b",0,"ZAP70Slp76PLCg_b",3,2).
action("cCbl",0,"cCblTCRlig",3,1).
action("TCRlig",0,"cCblTCRlig",3,2).
action("PLCg_a",0,"IP3",1,0).
action("PAGCsk",0,"PAGCskCD8CD45",6,2).
action("CD8",0,"PAGCskCD8CD45",6,4).
action("CD45",1,"PAGCskCD8CD45",6,7).
action("ERK",0,"Rsk",1,0).
action("DAG",1,"PKCth",0,1).
action("Fyn",0,"FynLCKTCRbind",7,3).
action("LCK",0,"FynLCKTCRbind",7,5).
action("TCRbind",0,"FynLCKTCRbind",7,6).
action("FosJun",3,"AP1",0,1).
action("cCbl",1,"cCblTCRphosLCK",0,4).
action("TCRphos",1,"cCblTCRphosLCK",0,2).
action("LCK",1,"cCblTCRphosLCK",0,1).
action("Grb2Sos",1,"Grb2SosRasGRP1",1,3).
action("RasGRP1",0,"Grb2SosRasGRP1",1,0).
action("LAT",1,"Gads",0,1).
action("Fos",0,"FosJun",3,1).
action("Jun",0,"FosJun",3,2).
action("PAGCsk",1,"PAGCskCD8CD45",3,7).
action("CD8",0,"PAGCskCD8CD45",3,1).
action("CD45",0,"PAGCskCD8CD45",3,2).
action("IkB",1,"NFkB",1,0).
action("CREB",0,"CRE",1,0).
action("ZAP70",1,"cCbl",0,1).
action("cCbl",0,"cCblTCRphosLCK",4,0).
action("TCRphos",1,"cCblTCRphosLCK",4,6).
action("LCK",1,"cCblTCRphosLCK",4,5).
action("Fyn",0,"FynLCKTCRbind",4,0).
action("LCK",1,"FynLCKTCRbind",4,6).
action("TCRbind",1,"FynLCKTCRbind",4,5).
action("Ca",1,"Calcin",0,1).
action("LCK",1,"Rlk",0,1).
action("ERK",1,"Fos",0,1).
action("Raf",0,"MEK",1,0).
action("PAGCsk",1,"PAGCskCD8CD45",0,4).
action("CD8",1,"PAGCskCD8CD45",0,2).
action("CD45",1,"PAGCskCD8CD45",0,1).
action("ZAP70",0,"ZAP70Slp76PLCg_b",6,2).
action("Slp76",0,"ZAP70Slp76PLCg_b",6,4).
action("PLCg_b",1,"ZAP70Slp76PLCg_b",6,7).
action("SEK",0,"JNK",1,0).
action("CD45",1,"CD45LCKTCRbind",0,4).
action("LCK",1,"CD45LCKTCRbind",0,2).
action("TCRbind",1,"CD45LCKTCRbind",0,1).
action("DAG",1,"DAGPKCth",1,3).
action("PKCth",0,"DAGPKCth",1,0).
action("LCK",0,"LCKTCRbind",2,0).
action("TCRbind",1,"LCKTCRbind",2,3).
action("Fyn",1,"FynLCKTCRbind",1,5).
action("LCK",1,"FynLCKTCRbind",1,3).
action("TCRbind",0,"FynLCKTCRbind",1,0).
action("TCRbind",1,"TCRbindFyn",1,3).
action("Fyn",0,"TCRbindFyn",1,0).
action("Itk",1,"ItkRlk",0,2).
action("Rlk",1,"ItkRlk",0,1).
action("TCRbindFyn",2,"PAGCsk",1,0).
action("CD45",0,"CD45LCKTCRbind",4,0).
action("LCK",1,"CD45LCKTCRbind",4,6).
action("TCRbind",1,"CD45LCKTCRbind",4,5).
action("JNK",1,"Jun",0,1).
action("CD45",0,"Fyn",1,0).
action("LCKTCRbind",0,"Fyn",1,0).
action("ZAP70",1,"ZAP70Slp76",1,3).
action("Slp76",0,"ZAP70Slp76",1,0).
action("PLCg_a",0,"DAG",1,0).
action("PKCth",0,"SEK",1,0).
action("ZAP70",1,"LAT",0,1).
action("ZAP70",1,"ZAP70Slp76PLCg_b",1,5).
action("Slp76",1,"ZAP70Slp76PLCg_b",1,3).
action("PLCg_b",0,"ZAP70Slp76PLCg_b",1,0).
action("Calcin",1,"NFAT",0,1).
action("IKK",0,"IkB",0,1).
action("Rsk",1,"CREB",0,1).
action("Fos",0,"FosJun",2,0).
action("Jun",1,"FosJun",2,3).
action("PKCth",1,"IKK",0,1).
action("Gads",1,"Slp76",0,1).
action("cCbl",1,"cCblTCRphosLCK",1,5).
action("TCRphos",1,"cCblTCRphosLCK",1,3).
action("LCK",0,"cCblTCRphosLCK",1,0).
action("Grb2Sos",0,"Grb2SosRasGRP1",2,0).
action("RasGRP1",1,"Grb2SosRasGRP1",2,3).
action("cCbl",0,"cCblTCRlig",2,0).
action("TCRlig",1,"cCblTCRlig",2,3).
action("PAGCskCD8CD45",3,"LCK",0,1).
action("LAT",0,"Gads",1,0).
action("cCbl",0,"cCblTCRphosLCK",5,1).
action("TCRphos",1,"cCblTCRphosLCK",5,7).
action("LCK",0,"cCblTCRphosLCK",5,4).
action("PAGCsk",0,"PAGCskCD8CD45",5,1).
action("CD8",1,"PAGCskCD8CD45",5,7).
action("CD45",0,"PAGCskCD8CD45",5,4).
action("cCblTCRphosLCK",3,"ZAP70",0,1).
action("ZAP70",0,"cCbl",1,0).
action("ZAP70",0,"ZAP70Slp76PLCg_b",4,0).
action("Slp76",1,"ZAP70Slp76PLCg_b",4,6).
action("PLCg_b",1,"ZAP70Slp76PLCg_b",4,5).
action("TCRbindFyn",0,"PAGCsk",0,1).
action("TCRbindFyn",1,"PAGCsk",0,1).
action("TCRbindFyn",3,"PAGCsk",0,1).
action("DAG",0,"PKCth",1,0).
action("Fyn",0,"FynLCKTCRbind",6,2).
action("LCK",0,"FynLCKTCRbind",6,4).
action("TCRbind",1,"FynLCKTCRbind",6,7).
action("Ras",1,"Raf",0,1).
action("CD45",1,"CD45LCKTCRbind",1,5).
action("LCK",1,"CD45LCKTCRbind",1,3).
action("TCRbind",0,"CD45LCKTCRbind",1,0).
action("LAT",1,"Grb2Sos",0,1).
action("LAT",0,"Grb2Sos",1,0).
action("PAGCsk",1,"PAGCskCD8CD45",2,6).
action("CD8",0,"PAGCskCD8CD45",2,0).
action("CD45",1,"PAGCskCD8CD45",2,3).
action("Slp76",0,"Itk",1,0).
action("ZAP70",0,"Itk",1,0).
action("Grb2SosRasGRP1",3,"Ras",0,1).
action("Grb2SosRasGRP1",1,"Ras",0,1).
action("Grb2SosRasGRP1",2,"Ras",0,1).
action("Fyn",1,"FynLCKTCRbind",3,7).
action("LCK",0,"FynLCKTCRbind",3,1).
action("TCRbind",0,"FynLCKTCRbind",3,2).
action("CD45",0,"CD45LCKTCRbind",5,1).
action("LCK",1,"CD45LCKTCRbind",5,7).
action("TCRbind",0,"CD45LCKTCRbind",5,4).
action("DAG",0,"DAGPKCth",2,0).
action("PKCth",1,"DAGPKCth",2,3).
action("IP3",1,"Ca",0,1).
action("MEK",0,"ERK",1,0).
action("LCK",1,"LCKTCRbind",1,3).
action("TCRbind",0,"LCKTCRbind",1,0).
action("Fos",1,"FosJun",1,3).
action("Jun",0,"FosJun",1,0).
action("TCRbind",1,"TCRbindFyn",0,2).
action("Fyn",1,"TCRbindFyn",0,1).
action("TCRbind",0,"TCRbindFyn",3,1).
action("Fyn",0,"TCRbindFyn",3,2).
action("Fyn",1,"TCRphos",0,1).
action("LCKTCRbind",3,"TCRphos",0,1).
action("Fyn",1,"FynLCKTCRbind",0,4).
action("LCK",1,"FynLCKTCRbind",0,2).
action("TCRbind",1,"FynLCKTCRbind",0,1).
action("ZAP70",0,"ZAP70Slp76PLCg_b",7,3).
action("Slp76",0,"ZAP70Slp76PLCg_b",7,5).
action("PLCg_b",0,"ZAP70Slp76PLCg_b",7,6).
action("PLCg_a",1,"IP3",0,1).
action("Calcin",0,"NFAT",1,0).
action("ZAP70",1,"ZAP70Slp76",0,2).
action("Slp76",1,"ZAP70Slp76",0,1).
action("Jun",0,"AP1",1,0).
action("Fos",0,"AP1",1,0).
action("FynLCKTCRbind",0,"TCRphos",1,0).
action("FynLCKTCRbind",1,"TCRphos",1,0).
action("FynLCKTCRbind",2,"TCRphos",1,0).
action("ERK",1,"Rsk",0,1).
action("Itk",0,"ItkRlk",3,1).
action("Rlk",0,"ItkRlk",3,2).
action("Rsk",0,"CREB",1,0).
action("ZAP70",0,"ZAP70Slp76",3,1).
action("Slp76",0,"ZAP70Slp76",3,2).
action("cCbl",1,"cCblTCRphosLCK",2,6).
action("TCRphos",0,"cCblTCRphosLCK",2,0).
action("LCK",1,"cCblTCRphosLCK",2,3).
action("Grb2Sos",0,"Grb2SosRasGRP1",3,1).
action("RasGRP1",0,"Grb2SosRasGRP1",3,2).
action("LCK",0,"Rlk",1,0).
action("CD45",0,"CD45",0,1).
action("ERK",0,"Fos",1,0).
action("CREB",1,"CRE",0,1).
action("cCbl",0,"cCblTCRphosLCK",6,2).
action("TCRphos",0,"cCblTCRphosLCK",6,4).
action("LCK",1,"cCblTCRphosLCK",6,7).
action("ZAP70",1,"ZAP70Slp76PLCg_b",2,6).
action("Slp76",0,"ZAP70Slp76PLCg_b",2,0).
action("PLCg_b",1,"ZAP70Slp76PLCg_b",2,3).
action("IP3",0,"Ca",1,0).
action("TCRlig",0,"TCRlig",0,1).
action("Raf",1,"MEK",0,1).
action("ZAP70Slp76PLCg_b",7,"__coop0",0,2).
action("ItkRlk",1,"__coop0",0,1).
action("ItkRlk",2,"__coop0",0,1).
action("ItkRlk",3,"__coop0",0,1).
action("cCbl",1,"cCblTCRlig",1,3).
action("TCRlig",0,"cCblTCRlig",1,0).
action("Gads",0,"Slp76",1,0).
action("__coop0",0,"PLCg_a",1,0).
action("__coop0",1,"PLCg_a",1,0).
action("__coop0",2,"PLCg_a",1,0).
action("PAGCsk",0,"PAGCskCD8CD45",7,3).
action("CD8",0,"PAGCskCD8CD45",7,5).
action("CD45",0,"PAGCskCD8CD45",7,6).
action("LAT",0,"PLCg_b",1,0).
action("SEK",1,"JNK",0,1).
action("CD45",1,"CD45LCKTCRbind",2,6).
action("LCK",0,"CD45LCKTCRbind",2,0).
action("TCRbind",1,"CD45LCKTCRbind",2,3).
action("ZAP70Slp76PLCg_b",7,"__coop0",1,3).
action("ItkRlk",0,"__coop0",1,0).
action("ZAP70Slp76PLCg_b",0,"__coop0",2,0).
action("ZAP70Slp76PLCg_b",1,"__coop0",2,0).
action("ZAP70Slp76PLCg_b",2,"__coop0",2,0).
action("ZAP70Slp76PLCg_b",3,"__coop0",2,0).
action("ZAP70Slp76PLCg_b",4,"__coop0",2,0).
action("ZAP70Slp76PLCg_b",5,"__coop0",2,0).
action("ZAP70Slp76PLCg_b",6,"__coop0",2,0).
action("ItkRlk",1,"__coop0",2,3).
action("ItkRlk",2,"__coop0",2,3).
action("ItkRlk",3,"__coop0",2,3).
action("CD8",0,"CD8",0,1).
action("JNK",0,"Jun",1,0).
action("ZAP70Slp76PLCg_b",0,"__coop0",3,1).
action("ZAP70Slp76PLCg_b",1,"__coop0",3,1).
action("ZAP70Slp76PLCg_b",2,"__coop0",3,1).
action("ZAP70Slp76PLCg_b",3,"__coop0",3,1).
action("ZAP70Slp76PLCg_b",4,"__coop0",3,1).
action("ZAP70Slp76PLCg_b",5,"__coop0",3,1).
action("ZAP70Slp76PLCg_b",6,"__coop0",3,1).
action("ItkRlk",0,"__coop0",3,2).
action("Fos",1,"FosJun",0,2).
action("Jun",1,"FosJun",0,1).
action("CD45",0,"CD45LCKTCRbind",6,2).
action("LCK",0,"CD45LCKTCRbind",6,4).
action("TCRbind",1,"CD45LCKTCRbind",6,7).
action("CD45LCKTCRbind",5,"Fyn",0,1).
action("CD45LCKTCRbind",6,"Fyn",0,1).
action("CD45LCKTCRbind",7,"Fyn",0,1).
action("PAGCsk",0,"PAGCskCD8CD45",4,0).
action("CD8",1,"PAGCskCD8CD45",4,6).
action("CD45",1,"PAGCskCD8CD45",4,5).
action("cCbl",1,"ZAP70",1,0).
action("TCRphos",0,"ZAP70",1,0).
action("LCK",0,"ZAP70",1,0).
action("PLCg_a",1,"DAG",0,1).
action("ZAP70",0,"LAT",1,0).
action("IKK",1,"IkB",1,0).
action("Fyn",0,"FynLCKTCRbind",5,1).
action("LCK",1,"FynLCKTCRbind",5,7).
action("TCRbind",0,"FynLCKTCRbind",5,4).
action("DAGPKCth",3,"RasGRP1",0,1).
action("PKCth",1,"SEK",0,1).
action("Itk",0,"ItkRlk",2,0).
action("Rlk",1,"ItkRlk",2,3).
action("cCblTCRlig",1,"TCRbind",0,1).
action("DAG",0,"DAGPKCth",3,1).
action("PKCth",0,"DAGPKCth",3,2).
action("ZAP70",0,"ZAP70Slp76PLCg_b",5,1).
action("Slp76",1,"ZAP70Slp76PLCg_b",5,7).
action("PLCg_b",0,"ZAP70Slp76PLCg_b",5,4).
action("DAG",0,"RasGRP1",1,0).
action("PKCth",0,"RasGRP1",1,0).
action("TCRlig",0,"TCRbind",1,0).
action("cCbl",1,"TCRbind",1,0).
action("PKCth",0,"IKK",1,0).
action("PAGCsk",1,"PAGCskCD8CD45",1,5).
action("CD8",1,"PAGCskCD8CD45",1,3).
action("CD45",0,"PAGCskCD8CD45",1,0).
action("Grb2Sos",1,"Grb2SosRasGRP1",0,2).
action("RasGRP1",1,"Grb2SosRasGRP1",0,1).
action("IkB",0,"NFkB",0,1).
action("Fyn",1,"FynLCKTCRbind",2,6).
action("LCK",0,"FynLCKTCRbind",2,0).
action("TCRbind",1,"FynLCKTCRbind",2,3).
action("LCK",1,"LCKTCRbind",0,2).
action("TCRbind",1,"LCKTCRbind",0,1).
action("CD8",0,"LCK",1,0).
action("CD45",0,"LCK",1,0).
action("PAGCsk",1,"LCK",1,0).
action("cCbl",1,"cCblTCRphosLCK",3,7).
action("TCRphos",0,"cCblTCRphosLCK",3,1).
action("LCK",0,"cCblTCRphosLCK",3,2).
action("LCK",0,"LCKTCRbind",3,1).
action("TCRbind",0,"LCKTCRbind",3,2).
action("TCRbind",0,"TCRbindFyn",2,0).
action("Fyn",1,"TCRbindFyn",2,3).
action("DAG",1,"DAGPKCth",0,2).
action("PKCth",1,"DAGPKCth",0,1).
action("__coop0",3,"PLCg_a",0,1).
action("LAT",1,"PLCg_b",0,1).
action("ZAP70",1,"ZAP70Slp76PLCg_b",0,4).
action("Slp76",1,"ZAP70Slp76PLCg_b",0,2).
action("PLCg_b",1,"ZAP70Slp76PLCg_b",0,1).
action("cCbl",0,"cCblTCRphosLCK",7,3).
action("TCRphos",0,"cCblTCRphosLCK",7,5).
action("LCK",0,"cCblTCRphosLCK",7,6).
action("ZAP70",0,"ZAP70Slp76",2,0).
action("Slp76",1,"ZAP70Slp76",2,3).
action("Ras",0,"Raf",1,0).
action("Ca",0,"Calcin",1,0).
action("CD45",1,"CD45LCKTCRbind",3,7).
action("LCK",0,"CD45LCKTCRbind",3,1).
action("TCRbind",0,"CD45LCKTCRbind",3,2).
action("Grb2SosRasGRP1",0,"Ras",1,0).
action("ZAP70Slp76",3,"Itk",0,1).
action("Itk",1,"ItkRlk",1,3).
action("Rlk",0,"ItkRlk",1,0).

% To be modified for the reachability problem  

% initialisation of active processes
init(actifProcess("AP1",0 )).
init(actifProcess("CD45",1 )).%++
init(actifProcess("CD45LCKTCRbind",0 )).
init(actifProcess("CD8",1 )).%++
init(actifProcess("CRE",0 )).
init(actifProcess("CREB",0 )).
init(actifProcess("Ca",0 )).
init(actifProcess("Calcin",0 )).
init(actifProcess("DAG",0 )).
init(actifProcess("DAGPKCth",0 )).
init(actifProcess("ERK",0 )).
init(actifProcess("Fos",0 )).
init(actifProcess("FosJun",0 )).
init(actifProcess("Fyn",0 )).
init(actifProcess("FynLCKTCRbind",0 )).
init(actifProcess("Gads",0 )).
init(actifProcess("Grb2Sos",0 )).
init(actifProcess("Grb2SosRasGRP1",0 )).
init(actifProcess("IKK",0 )).
init(actifProcess("IP3",0 )).
init(actifProcess("IkB",0 )).
init(actifProcess("Itk",0 )).
init(actifProcess("ItkRlk",0 )).
init(actifProcess("JNK",0 )).
init(actifProcess("Jun",0 )).
init(actifProcess("LAT",0 )).
init(actifProcess("LCK",0 )).
init(actifProcess("LCKTCRbind",0 )).
init(actifProcess("MEK",0 )).
init(actifProcess("NFAT",0 )).
init(actifProcess("NFkB",0 )).
init(actifProcess("PAGCsk",0 )).
init(actifProcess("PAGCskCD8CD45",0 )).
init(actifProcess("PKCth",0 )).
init(actifProcess("PLCg_a",0 )).
init(actifProcess("PLCg_b",0 )).
init(actifProcess("Raf",0 )).
init(actifProcess("Ras",0 )).
init(actifProcess("RasGRP1",0 )).
init(actifProcess("Rlk",0 )).
init(actifProcess("Rsk",0 )).
init(actifProcess("SEK",0 )).
init(actifProcess("Slp76",0 )).
init(actifProcess("TCRbind",0 )).
init(actifProcess("TCRbindFyn",0 )).
init(actifProcess("TCRlig",1 )).%++
init(actifProcess("TCRphos",0 )).
init(actifProcess("ZAP70",0 )).
init(actifProcess("ZAP70Slp76",0 )).
init(actifProcess("ZAP70Slp76PLCg_b",0 )).
init(actifProcess("__coop0",0 )).
init(actifProcess("cCbl",0 )).
init(actifProcess("cCblTCRlig",0 )).
init(actifProcess("cCblTCRphosLCK",0 )).

% List of processes to be reached

goal(actifProcess("AP1", 0 )).
goal(actifProcess("CD45", 1 )).
goal(actifProcess("CD8", 1 )).
goal(actifProcess("CRE", 0 )).
goal(actifProcess("CREB", 0 )).
goal(actifProcess("Ca", 1 )).
goal(actifProcess("Calcin", 1 )).
goal(actifProcess("DAG", 0 )).
goal(actifProcess("ERK", 0 )).
goal(actifProcess("Fos", 0 )).
goal(actifProcess("Fyn", 1 )).
goal(actifProcess("Gads", 1 )).
goal(actifProcess("Grb2Sos", 0 )).
goal(actifProcess("IKK", 0 )).
goal(actifProcess("IP3", 1 )).
goal(actifProcess("IkB", 0 )).
goal(actifProcess("Itk", 0 )).
goal(actifProcess("JNK", 0 )).
goal(actifProcess("Jun", 0 )).
goal(actifProcess("LAT", 1 )).
goal(actifProcess("LCK", 1 )). %++
goal(actifProcess("MEK", 0 )).
goal(actifProcess("NFAT", 1 )).
goal(actifProcess("NFkB", 1 )).
goal(actifProcess("PAGCsk", 0 )). %%%
goal(actifProcess("PKCth", 0 )).%%%
goal(actifProcess("PLCg_a", 1 )).
goal(actifProcess("PLCg_b", 1 )).
goal(actifProcess("Raf", 0 )).%%%
goal(actifProcess("Ras", 0 )).%%%
goal(actifProcess("RasGRP1", 0 )).
goal(actifProcess("Rlk", 1 )). %++
goal(actifProcess("Rsk", 0 )). %%%
goal(actifProcess("SEK", 0 )). %%%
goal(actifProcess("Slp76", 1 )).
goal(actifProcess("TCRbind", 0 )). %%%
goal(actifProcess("TCRlig", 1 )).
goal(actifProcess("TCRphos", 1 )).
goal(actifProcess("ZAP70", 1 )).
goal(actifProcess("cCbl", 0 )). %%%%

%----------------------
% Fixed point identification:
%----------------------

	% $ ./clingo fixed-points.lp tcrsig40_whole-state.lp

%----------------------
% Reachability command:
%----------------------
	%
	% ***** 
	% iterative method:
	% *****
		% $ ./clingo reachability-iterative.lp incmode-int.lp tcrsig40_whole-state.lp
	%
	% *****
	% non-iterative method:
	% *****
		% $ ./clingo reachability-fixed-T.lp tcrsig40_whole-state.lp

% --------
% Results
% --------

% *****
% Fixed point:
% *****
% fixProcess("LCK",0) fixProcess("TCRlig",1) fixProcess("ERK",0) fixProcess("Slp76",0) fixProcess("PLCg_b",0) fixProcess("cCbl",0) fixProcess("PLCg_a",0) fixProcess("CD45",1) fixProcess("PKCth",0) fixProcess("AP1",0) fixProcess("TCRphos",1) fixProcess("RasGRP1",0) fixProcess("Gads",0) fixProcess("Fos",0) fixProcess("Jun",0) fixProcess("PAGCsk",1) fixProcess("IkB",1) fixProcess("CREB",0) fixProcess("TCRbind",1) fixProcess("Calcin",0) fixProcess("Rlk",0) fixProcess("Raf",0) fixProcess("CD8",1) fixProcess("ZAP70",0) fixProcess("SEK",0) fixProcess("Fyn",1) fixProcess("ItkRlk",0) fixProcess("LAT",0) fixProcess("NFAT",0) fixProcess("IKK",0) fixProcess("Grb2Sos",0) fixProcess("TCRbindFyn",3) fixProcess("DAG",0) fixProcess("Ras",0) fixProcess("CD45LCKTCRbind",5) fixProcess("Ca",0) fixProcess("MEK",0) fixProcess("LCKTCRbind",1) fixProcess("IP3",0) fixProcess("ZAP70Slp76",0) fixProcess("Rsk",0) fixProcess("Itk",0) fixProcess("cCblTCRphosLCK",2) fixProcess("CRE",0) fixProcess("__coop0",0) fixProcess("cCblTCRlig",1) fixProcess("PAGCskCD8CD45",7) fixProcess("JNK",0) fixProcess("ZAP70Slp76PLCg_b",0) fixProcess("FosJun",0) fixProcess("FynLCKTCRbind",5) fixProcess("Grb2SosRasGRP1",0) fixProcess("NFkB",0) fixProcess("DAGPKCth",0)

% *****
% Path to activate goals:
% *****
%actifFromTo("PAGCskCD8CD45",0,2,0) actifFromTo("PAGCskCD8CD45",2,3,1) actifFromTo("LCK",0,1,2) actifFromTo("CD45LCKTCRbind",0,2,3) actifFromTo("CD45LCKTCRbind",2,6,4) actifFromTo("Fyn",0,1,5) actifFromTo("TCRphos",0,1,6) actifFromTo("cCblTCRphosLCK",0,2,7) actifFromTo("cCblTCRphosLCK",2,3,8) actifFromTo("ZAP70",0,1,9) actifFromTo("LAT",0,1,10) actifFromTo("PLCg_b",0,1,11) actifFromTo("ZAP70Slp76PLCg_b",0,1,12) actifFromTo("NFkB",0,1,13) actifFromTo("Rlk",0,1,14) actifFromTo("Gads",0,1,15) actifFromTo("ItkRlk",0,1,16) actifFromTo("__coop0",0,1,17) actifFromTo("ZAP70Slp76PLCg_b",1,5,18) actifFromTo("Slp76",0,1,19) actifFromTo("ZAP70Slp76PLCg_b",5,7,20) actifFromTo("__coop0",1,3,21) actifFromTo("PLCg_a",0,1,22) actifFromTo("IP3",0,1,23) actifFromTo("Ca",0,1,24) actifFromTo("Calcin",0,1,25) actifFromTo("NFAT",0,1,26) 
%