1. verilog_re_match is for using re to pasrsing verilog code and modify code to remove some init value to avoid irun report error message when run simultation.

error message in below
```
ncelab: 15.20-s084: (c) Copyright 1995-2020 Cadence Design Systems, Inc.
ncelab: *W,DSEMEL: This SystemVerilog design will be simulated as per IEEE 1800-2009 SystemVerilog simulation semantics. Use -disable_sem2009 option for turning off SV 2009 simulation semantics.
always_comb begin
          |
ncelab: *E,MULAXX (/home/raid7_2/userp/b0126168/tony/University_LAB/lab_formal_release/common/caravel_project/rtl/verilog/mgmt_core.patrick.v,4971|10): Multiple drivers to always_comb output variable mgmtsoc_soc_rst detected.
always_comb begin
          |
```
