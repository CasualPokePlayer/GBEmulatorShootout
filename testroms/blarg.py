from test import *


all = [
    Test("blarg/cpu_instrs/01-special.gb", runtime=3.0),
    Test("blarg/cpu_instrs/02-interrupts.gb", runtime=1.0),
    Test("blarg/cpu_instrs/03-op_sp,hl.gb", runtime=2.5),
    Test("blarg/cpu_instrs/04-op_r,imm.gb", runtime=2.5),
    Test("blarg/cpu_instrs/05-op_rp.gb", runtime=3.0),
    Test("blarg/cpu_instrs/06-ld_r,r.gb", runtime=1.0),
    Test("blarg/cpu_instrs/07-jr,jp,call,ret,rst.gb", runtime=1.0),
    Test("blarg/cpu_instrs/08-misc_instrs.gb", runtime=1.0),
    Test("blarg/cpu_instrs/09-op_r,r.gb", runtime=7.0),
    Test("blarg/cpu_instrs/10-bit_ops.gb", runtime=14.0),
    Test("blarg/cpu_instrs/11-op_a,(hl).gb", runtime=13.0),

    Test("blarg/halt_bug.gb", runtime=2.0),
    Test("blarg/instr_timing.gb", runtime=1.0),
    Test("blarg/interrupt_time.gb", runtime=1.5, model=CGB), # Note, on DMG there is an write to VRAM while it is blocked

    Test("blarg/mem_timing/01-read_timing.gb", runtime=1.0),
    Test("blarg/mem_timing/02-write_timing.gb", runtime=1.0),
    Test("blarg/mem_timing/03-modify_timing.gb", runtime=1.0),

    Test("blarg/mem_timing-2/01-read_timing.gb", runtime=1.0),
    Test("blarg/mem_timing-2/02-write_timing.gb", runtime=1.0),
    Test("blarg/mem_timing-2/03-modify_timing.gb", runtime=1.0),

    Test("blarg/oam_bug/1-lcd_sync.gb", runtime=1.0),
    Test("blarg/oam_bug/2-causes.gb", runtime=1.0),
    Test("blarg/oam_bug/3-non_causes.gb", runtime=3.0),
    Test("blarg/oam_bug/4-scanline_timing.gb", runtime=1.5),
    Test("blarg/oam_bug/5-timing_bug.gb", runtime=1.5),
    Test("blarg/oam_bug/6-timing_no_bug.gb", runtime=1.5),
    # Test("blarg/oam_bug/7-timing_effect.gb", runtime=8.5), # This test is broken.
    Test("blarg/oam_bug/8-instr_effect.gb", runtime=1.5),

    Test("blarg/dmg_sound/01-registers.gb", runtime=2.0),
    Test("blarg/dmg_sound/02-len_ctr.gb", runtime=11.0),
    Test("blarg/dmg_sound/03-trigger.gb", runtime=18.0),
    Test("blarg/dmg_sound/04-sweep.gb", runtime=2.0),
    Test("blarg/dmg_sound/05-sweep_details.gb", runtime=2.0),
    Test("blarg/dmg_sound/06-overflow_on_trigger.gb", runtime=2.0),
    Test("blarg/dmg_sound/07-len_sweep_period_sync.gb", runtime=2.0),
    Test("blarg/dmg_sound/08-len_ctr_during_power.gb", runtime=2.0),
    Test("blarg/dmg_sound/09-wave_read_while_on.gb", runtime=1.0),
    Test("blarg/dmg_sound/10-wave_trigger_while_on.gb", runtime=5.0),
    Test("blarg/dmg_sound/11-regs_after_power.gb", runtime=1.0),
    Test("blarg/dmg_sound/12-wave_write_while_on.gb", runtime=5.0),

    Test("blarg/cgb_sound/01-registers.gb", runtime=1.5, model=CGB),
    Test("blarg/cgb_sound/02-len_ctr.gb", runtime=11.0, model=CGB),
    Test("blarg/cgb_sound/03-trigger.gb", runtime=18.0, model=CGB),
    Test("blarg/cgb_sound/04-sweep.gb", runtime=2.5, model=CGB),
    Test("blarg/cgb_sound/05-sweep_details.gb", runtime=12.0, model=CGB),
    Test("blarg/cgb_sound/06-overflow_on_trigger.gb", runtime=2.0, model=CGB),
    Test("blarg/cgb_sound/07-len_sweep_period_sync.gb", runtime=1.5, model=CGB),
    Test("blarg/cgb_sound/08-len_ctr_during_power.gb", runtime=3.5, model=CGB),
    Test("blarg/cgb_sound/09-wave_read_while_on.gb", runtime=1.5, model=CGB),
    Test("blarg/cgb_sound/10-wave_trigger_while_on.gb", runtime=5.0, model=CGB),
    Test("blarg/cgb_sound/11-regs_after_power.gb", runtime=1.5, model=CGB),
    Test("blarg/cgb_sound/12-wave.gb", runtime=1.5, model=CGB),
]
