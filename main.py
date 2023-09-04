import os
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivy.uix.label import Label
from components.mi8tAV.mi8AV import mi8tAV
from components.mi8tQI.mi8QI import mi8tQI
from components.mi8amtAV.mi8aAV import mi8amtAV
from components.mi8amtQI.mi8aQI import mi8amtQI
from components.mi8tAV.mi8tAV_pojar.mi8tAV_pojar import mi8tAV_pojar
from components.mi8tAV.mi8tAV_pojar.mi8tAV_pojar_zemlya.mi8tAV_pojar_zemlya import mi8tAV_pojar_zemlya
from components.mi8tAV.mi8tAV_pojar_VR.mi8tAV_pojar_VR import mi8tAV_pojar_VR
from components.mi8tAV.mi8tAV_pojar_VR.mi8tAV_pojar_VR_zemlya.mi8tAV_pojar_VR_zemlya import mi8tAV_pojar_VR_zemlya
from components.mi8tAV.mi8tAV_pojar_KO.mi8tAV_pojar_KO import mi8tAV_pojar_KO
from components.mi8tAV.mi8tAV_pojar_KO.mi8tAV_pojar_KO_zemlya.mi8tAV_pojar_KO_zemlya import mi8tAV_pojar_KO_zemlya
from components.mi8tAV.mi8tAV_pojar_cab.mi8tAV_pojar_cab import mi8tAV_pojar_cab
from components.mi8tAV.mi8tAV_pojar_cab.mi8tAV_pojar_cab_zemlya.mi8tAV_pojar_cab_zemlya import mi8tAV_pojar_cab_zemlya
from components.mi8tAV.mi8tAV_1dv.mi8tAV_1dv import mi8tAV_1dv
from components.mi8tAV.mi8tAV_1dv_malH.mi8tAV_1dv_malH import mi8tAV_1dv_malH
from components.mi8tAV.mi8tAV_2dv.mi8tAV_2dv import mi8tAV_2dv
from components.mi8tAV.mi8tAV_ogs.mi8tAV_ogs import mi8tAV_ogs
from components.mi8tAV.mi8tAV_pu.mi8tAV_pu import mi8tAV_pu
from components.mi8tAV.mi8tAV_system.mi8tAV_system import mi8tAV_system
from components.mi8tAV.mi8tAV_strujka.mi8tAV_strujka import mi8tAV_strujka
from components.mi8tAV.mi8tAV_vibro.mi8tAV_vibro import mi8tAV_vibro
from components.mi8tAV.mi8tAV_XR_PR.mi8tAV_XR_PR import mi8tAV_XR_PR
from components.mi8tAV.mi8tAV_maslo_dv.mi8tAV_maslo_dv import mi8tAV_maslo_dv
from components.mi8tAV.mi8tAV_drenaj.mi8tAV_drenaj import mi8tAV_drenaj
from components.mi8tAV.mi8tAV_sbros.mi8tAV_sbros import mi8tAV_sbros
from components.mi8tAV.mi8tAV_susha.mi8tAV_susha import mi8tAV_susha
from components.mi8tAV.mi8tAV_voda.mi8tAV_voda import mi8tAV_voda
from components.mi8tAV.mi8tAV_pu2.mi8tAV_pu2 import mi8tAV_pu2
from components.mi8tAV.mi8tAV_SAR.mi8tAV_SAR import mi8tAV_SAR
from components.mi8tAV.mi8tAV_ZEM.mi8tAV_ZEM import mi8tAV_ZEM
from components.mi8tAV.mi8tAV_2nRB.mi8tAV_2nRB import mi8tAV_2nRB
from components.mi8tAV.mi8tAV_2gen.mi8tAV_2gen import mi8tAV_2gen
from components.mi8tAV.mi8tAV_sgo.mi8tAV_sgo import mi8tAV_sgo
from components.mi8tAV.mi8tAV_agb.mi8tAV_agb import mi8tAV_agb
from components.mi8tAV.mi8tAV_2us.mi8tAV_2us import mi8tAV_2us
from components.mi8tAV.mi8tAV_270.mi8tAV_270 import mi8tAV_270
from components.mi8tAV.mi8tAV_vk.mi8tAV_vk import mi8tAV_vk
from components.mi8tAV.mi8tAV_Pvibro.mi8tAV_Pvibro import mi8tAV_Pvibro
from components.mi8tAV.mi8tAV_NHV.mi8tAV_NHV import mi8tAV_NHV
from components.mi8tAV.mi8tAV_1nRB.mi8tAV_1nRB import mi8tAV_1nRB
from components.mi8tAV.mi8tAV_1gen.mi8tAV_1gen import mi8tAV_1gen
from components.mi8tAV.mi8tAV_RS.mi8tAV_RS import mi8tAV_RS
from components.mi8tAV.mi8tAV_1us.mi8tAV_1us import mi8tAV_1us
from components.mi8tAV.mi8tAV_popKlap.mi8tAV_popKlap import mi8tAV_popKlap
from components.mi8tAV.mi8tAV_MEL.mi8tAV_MEL import mi8tAV_MEL
from components.mi8tAV.mi8tAV_MEL.mi8tAV_obshivka.mi8tAV_obshivka import mi8tAV_obshivka
from components.mi8tAV.mi8tAV_MEL.mi8tAV_steklo.mi8tAV_steklo import mi8tAV_steklo
from components.mi8tAV.mi8tAV_MEL.mi8tAV_emt2.mi8tAV_emt2 import mi8tAV_emt2
from components.mi8tAV.mi8tAV_MEL.mi8tAV_ecn75.mi8tAV_ecn75 import mi8tAV_ecn75
from components.mi8tAV.mi8tAV_MEL.mi8tAV_toplivomer.mi8tAV_toplivomer import mi8tAV_toplivomer
from components.mi8tAV.mi8tAV_MEL.mi8tAV_ko50.mi8tAV_ko50 import mi8tAV_ko50
from components.mi8tAV.mi8tAV_MEL.mi8tAV_rio3.mi8tAV_rio3 import mi8tAV_rio3
from components.mi8tAV.mi8tAV_MEL.mi8tAV_genpost.mi8tAV_genpost import mi8tAV_genpost
from components.mi8tAV.mi8tAV_MEL.mi8tAV_genper.mi8tAV_genper import mi8tAV_genper
from components.mi8tAV.mi8tAV_MEL.mi8tAV_svet.mi8tAV_svet import mi8tAV_svet
from components.mi8tAV.mi8tAV_MEL.mi8tAV_siggen.mi8tAV_siggen import mi8tAV_siggen
from components.mi8tAV.mi8tAV_MEL.mi8tAV_lamp.mi8tAV_lamp import mi8tAV_lamp
from components.mi8tAV.mi8tAV_MEL.mi8tAV_posfar.mi8tAV_posfar import mi8tAV_posfar
from components.mi8tAV.mi8tAV_MEL.mi8tAV_rulfar.mi8tAV_rulfar import mi8tAV_rulfar
from components.mi8tAV.mi8tAV_MEL.mi8tAV_ano.mi8tAV_ano import mi8tAV_ano
from components.mi8tAV.mi8tAV_MEL.mi8tAV_mayak.mi8tAV_mayak import mi8tAV_mayak
from components.mi8tAV.mi8tAV_MEL.mi8tAV_us.mi8tAV_us import mi8tAV_us
from components.mi8tAV.mi8tAV_MEL.mi8tAV_vd.mi8tAV_vd import mi8tAV_vd
from components.mi8tAV.mi8tAV_MEL.mi8tAV_var.mi8tAV_var import mi8tAV_var
from components.mi8tAV.mi8tAV_MEL.mi8tAV_ki13.mi8tAV_ki13 import mi8tAV_ki13
from components.mi8tAV.mi8tAV_MEL.mi8tAV_rv.mi8tAV_rv import mi8tAV_rv
from components.mi8tAV.mi8tAV_MEL.mi8tAV_u2.mi8tAV_u2 import mi8tAV_u2
from components.mi8tAV.mi8tAV_MEL.mi8tAV_ark9.mi8tAV_ark9 import mi8tAV_ark9
from components.mi8tAV.mi8tAV_MEL.mi8tAV_spu7.mi8tAV_spu7 import mi8tAV_spu7
from components.mi8tAV.mi8tAV_MEL.mi8tAV_ukv.mi8tAV_ukv import mi8tAV_ukv
from components.mi8tAV.mi8tAV_MEL.mi8tAV_kv.mi8tAV_kv import mi8tAV_kv
from components.mi8tQI.mi8QI_ogr.mi8QI_ogr import mi8QI_ogr
from components.mi8tQI.mi8QI_ogr.mi8QI_min.mi8QI_min import mi8QI_min
from components.mi8tQI.mi8QI_ogr.mi8QI_mas.mi8QI_mas import mi8QI_mas
from components.mi8tQI.mi8QI_ogr.mi8QI_veter.mi8QI_veter import mi8QI_veter
from components.mi8tQI.mi8QI_ogr.mi8QI_skor.mi8QI_skor import mi8QI_skor
from components.mi8tQI.mi8QI_ogr.mi8QI_nv.mi8QI_nv import mi8QI_nv
from components.mi8tQI.mi8QI_ogr.mi8QI_man.mi8QI_man import mi8QI_man
from components.mi8tQI.mi8QI_ogr.mi8QI_ogr1.mi8QI_ogr1 import mi8QI_ogr1
from components.mi8tQI.mi8QI_ogr.mi8QI_plosh.mi8QI_plosh import mi8QI_plosh

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_plosh/mi8QI_plosh.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_ogr1/mi8QI_ogr1.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_man/mi8QI_man.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_nv/mi8QI_nv.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_skor/mi8QI_skor.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_veter/mi8QI_veter.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_mas/mi8QI_mas.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_min/mi8QI_min.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI_ogr/mi8QI_ogr.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_kv/mi8tAV_kv.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_ukv/mi8tAV_ukv.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_spu7/mi8tAV_spu7.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_ark9/mi8tAV_ark9.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_u2/mi8tAV_u2.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_rv/mi8tAV_rv.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_ki13/mi8tAV_ki13.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_var/mi8tAV_var.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_vd/mi8tAV_vd.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_us/mi8tAV_us.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_mayak/mi8tAV_mayak.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_ano/mi8tAV_ano.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_rulfar/mi8tAV_rulfar.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_posfar/mi8tAV_posfar.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_lamp/mi8tAV_lamp.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_siggen/mi8tAV_siggen.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_svet/mi8tAV_svet.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_genper/mi8tAV_genper.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_genpost/mi8tAV_genpost.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_rio3/mi8tAV_rio3.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_ko50/mi8tAV_ko50.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_toplivomer/mi8tAV_toplivomer.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_ecn75/mi8tAV_ecn75.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_emt2/mi8tAV_emt2.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_steklo/mi8tAV_steklo.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_obshivka/mi8tAV_obshivka.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_MEL/mi8tAV_MEL.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_popKlap/mi8tAV_popKlap.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_1us/mi8tAV_1us.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_RS/mi8tAV_RS.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_1gen/mi8tAV_1gen.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_1nRB/mi8tAV_1nRB.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_NHV/mi8tAV_NHV.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_Pvibro/mi8tAV_Pvibro.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_vk/mi8tAV_vk.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_270/mi8tAV_270.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_2us/mi8tAV_2us.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_agb/mi8tAV_agb.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_sgo/mi8tAV_sgo.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_2gen/mi8tAV_2gen.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_2nRB/mi8tAV_2nRB.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_ZEM/mi8tAV_ZEM.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_SAR/mi8tAV_SAR.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pu2/mi8tAV_pu2.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_voda/mi8tAV_voda.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_susha/mi8tAV_susha.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_sbros/mi8tAV_sbros.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_drenaj/mi8tAV_drenaj.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_XR_PR/mi8tAV_XR_PR.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_vibro/mi8tAV_vibro.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_strujka/mi8tAV_strujka.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_system/mi8tAV_system.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pu/mi8tAV_pu.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_ogs/mi8tAV_ogs.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_2dv/mi8tAV_2dv.kv'.format(
    root if root != '' else os.getcwd())
)


root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_1dv_malH/mi8tAV_1dv_malH.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_1dv/mi8tAV_1dv.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar_cab/mi8tAV_pojar_cab_zemlya/mi8tAV_pojar_cab_zemlya.kv'.format(
    root if root != '' else os.getcwd())
)


root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar_cab/mi8tAV_pojar_cab.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar_KO/mi8tAV_pojar_KO_zemlya/mi8tAV_pojar_KO_zemlya.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar_KO/mi8tAV_pojar_KO.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar_VR/mi8tAV_pojar_VR_zemlya/mi8tAV_pojar_VR_zemlya.kv'.format(
    root if root != '' else os.getcwd())
)


root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar_VR/mi8tAV_pojar_VR.kv'.format(
    root if root != '' else os.getcwd())
)


root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar/mi8tAV_pojar_zemlya/mi8tAV_pojar_zemlya.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8tAV_pojar/mi8tAV_pojar.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tAV/mi8AV.kv'.format(
    root if root != '' else os.getcwd())
)
root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8tQI/mi8QI.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8amtAV/mi8aAV.kv'.format(
    root if root != '' else os.getcwd())
)

root = os.path.split(__file__)[0]
Builder.load_file('{}/components/mi8amtQI/mi8aQI.kv'.format(
    root if root != '' else os.getcwd())
)



class mainScreen(Screen):
    pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        sm = ScreenManager()
        sm.add_widget(mainScreen(name="mainScreen"))
        sm.add_widget(mi8tAV(name="Mi8tAV"))
        sm.add_widget(mi8tQI(name="Mi8tQI"))
        sm.add_widget(mi8amtAV(name="Mi8amtAV"))
        sm.add_widget(mi8amtQI(name="Mi8amtQI"))
        sm.add_widget(mi8tAV_pojar(name="Mi8tAV_pojar"))
        sm.add_widget(mi8tAV_pojar_zemlya(name="Mi8tAV_pojar_zemlya"))
        sm.add_widget(mi8tAV_pojar_VR(name="Mi8tAV_pojar_VR"))
        sm.add_widget(mi8tAV_pojar_VR_zemlya(name="Mi8tAV_pojar_VR_zemlya"))
        sm.add_widget(mi8tAV_pojar_KO(name="Mi8tAV_pojar_KO"))
        sm.add_widget(mi8tAV_pojar_KO_zemlya(name="Mi8tAV_pojar_KO_zemlya"))
        sm.add_widget(mi8tAV_pojar_cab(name="Mi8tAV_pojar_cab"))
        sm.add_widget(mi8tAV_pojar_cab_zemlya(name="Mi8tAV_pojar_cab_zemlya"))
        sm.add_widget(mi8tAV_1dv(name="Mi8tAV_1dv"))
        sm.add_widget(mi8tAV_1dv_malH(name="Mi8tAV_1dv_malH"))
        sm.add_widget(mi8tAV_2dv(name="Mi8tAV_2dv"))
        sm.add_widget(mi8tAV_ogs(name="Mi8tAV_ogs"))
        sm.add_widget(mi8tAV_pu(name="Mi8tAV_pu"))
        sm.add_widget(mi8tAV_system(name="Mi8tAV_system"))
        sm.add_widget(mi8tAV_strujka(name="Mi8tAV_strujka"))
        sm.add_widget(mi8tAV_vibro(name="Mi8tAV_vibro"))
        sm.add_widget(mi8tAV_XR_PR(name="Mi8tAV_XR_PR"))
        sm.add_widget(mi8tAV_maslo_dv(name="Mi8tAV_maslo_dv"))
        sm.add_widget(mi8tAV_drenaj(name="Mi8tAV_drenaj"))
        sm.add_widget(mi8tAV_sbros(name="Mi8tAV_sbros"))
        sm.add_widget(mi8tAV_susha(name="Mi8tAV_susha"))
        sm.add_widget(mi8tAV_voda(name="Mi8tAV_voda"))
        sm.add_widget(mi8tAV_pu2(name="Mi8tAV_pu2"))
        sm.add_widget(mi8tAV_SAR(name="Mi8tAV_SAR"))
        sm.add_widget(mi8tAV_ZEM(name="Mi8tAV_ZEM"))
        sm.add_widget(mi8tAV_2nRB(name="Mi8tAV_2nRB"))
        sm.add_widget(mi8tAV_2gen(name="Mi8tAV_2gen"))
        sm.add_widget(mi8tAV_sgo(name="Mi8tAV_sgo"))
        sm.add_widget(mi8tAV_agb(name="Mi8tAV_agb"))
        sm.add_widget(mi8tAV_2us(name="Mi8tAV_2us"))
        sm.add_widget(mi8tAV_270(name="Mi8tAV_270"))
        sm.add_widget(mi8tAV_vk(name="Mi8tAV_vk"))
        sm.add_widget(mi8tAV_Pvibro(name="Mi8tAV_Pvibro"))
        sm.add_widget(mi8tAV_NHV(name="Mi8tAV_NHV"))
        sm.add_widget(mi8tAV_1nRB(name="Mi8tAV_1nRB"))
        sm.add_widget(mi8tAV_1gen(name="Mi8tAV_1gen"))
        sm.add_widget(mi8tAV_RS(name="Mi8tAV_RS"))
        sm.add_widget(mi8tAV_1us(name="Mi8tAV_1us"))
        sm.add_widget(mi8tAV_popKlap(name="Mi8tAV_popKlap"))
        sm.add_widget(mi8tAV_MEL(name="Mi8tAV_MEL"))
        sm.add_widget(mi8tAV_obshivka(name="Mi8tAV_obshivka"))
        sm.add_widget(mi8tAV_steklo(name="Mi8tAV_steklo"))
        sm.add_widget(mi8tAV_emt2(name="Mi8tAV_emt2"))
        sm.add_widget(mi8tAV_ecn75(name="Mi8tAV_ecn75"))
        sm.add_widget(mi8tAV_toplivomer(name="Mi8tAV_toplivomer"))
        sm.add_widget(mi8tAV_ko50(name="Mi8tAV_ko50"))
        sm.add_widget(mi8tAV_rio3(name="Mi8tAV_rio3"))
        sm.add_widget(mi8tAV_genpost(name="Mi8tAV_genpost"))
        sm.add_widget(mi8tAV_genper(name="Mi8tAV_genper"))
        sm.add_widget(mi8tAV_svet(name="Mi8tAV_svet"))
        sm.add_widget(mi8tAV_siggen(name="Mi8tAV_siggen"))
        sm.add_widget(mi8tAV_lamp(name="Mi8tAV_lamp"))
        sm.add_widget(mi8tAV_posfar(name="Mi8tAV_posfar"))
        sm.add_widget(mi8tAV_rulfar(name="Mi8tAV_rulfar"))
        sm.add_widget(mi8tAV_ano(name="Mi8tAV_ano"))
        sm.add_widget(mi8tAV_mayak(name="Mi8tAV_mayak"))
        sm.add_widget(mi8tAV_us(name="Mi8tAV_us"))
        sm.add_widget(mi8tAV_vd(name="Mi8tAV_vd"))
        sm.add_widget(mi8tAV_var(name="Mi8tAV_var"))
        sm.add_widget(mi8tAV_ki13(name="Mi8tAV_ki13"))
        sm.add_widget(mi8tAV_rv(name="Mi8tAV_rv"))
        sm.add_widget(mi8tAV_u2(name="Mi8tAV_u2"))
        sm.add_widget(mi8tAV_ark9(name="Mi8tAV_ark9"))
        sm.add_widget(mi8tAV_spu7(name="Mi8tAV_spu7"))
        sm.add_widget(mi8tAV_ukv(name="Mi8tAV_ukv"))
        sm.add_widget(mi8tAV_kv(name="Mi8tAV_kv"))
        sm.add_widget(mi8QI_ogr(name="Mi8QI_ogr"))
        sm.add_widget(mi8QI_min(name="Mi8QI_min"))
        sm.add_widget(mi8QI_mas(name="Mi8QI_mas"))
        sm.add_widget(mi8QI_veter(name="Mi8QI_veter"))
        sm.add_widget(mi8QI_skor(name="Mi8QI_skor"))
        sm.add_widget(mi8QI_nv(name="Mi8QI_nv"))
        sm.add_widget(mi8QI_man(name="Mi8QI_man"))
        sm.add_widget(mi8QI_ogr1(name="Mi8QI_ogr1"))
        sm.add_widget(mi8QI_plosh(name="Mi8QI_plosh"))
        return sm



if __name__ == '__main__':
    MyApp().run()