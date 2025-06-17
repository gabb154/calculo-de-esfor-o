import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
from io import BytesIO

# ==============================================================================
# BANCO DE DADOS INTERNO (COMPLETO E SEPARADO POR TIPO)
# ==============================================================================

DB_SECUNDARIA = [
    {'FASES': 3, 'CABO': 120, 'VAO_M': 5, 'Y_DAN': 10}, {'FASES': 3, 'CABO': 120, 'VAO_M': 10, 'Y_DAN': 40},
    {'FASES': 3, 'CABO': 120, 'VAO_M': 15, 'Y_DAN': 88}, {'FASES': 3, 'CABO': 120, 'VAO_M': 20, 'Y_DAN': 156},
    {'FASES': 3, 'CABO': 120, 'VAO_M': 25, 'Y_DAN': 244}, {'FASES': 3, 'CABO': 120, 'VAO_M': 30, 'Y_DAN': 351},
    {'FASES': 3, 'CABO': 120, 'VAO_M': 35, 'Y_DAN': 478}, {'FASES': 3, 'CABO': 120, 'VAO_M': 40, 'Y_DAN': 527},
    {'FASES': 3, 'CABO': 70, 'VAO_M': 5, 'Y_DAN': 7}, {'FASES': 3, 'CABO': 70, 'VAO_M': 10, 'Y_DAN': 26},
    {'FASES': 3, 'CABO': 70, 'VAO_M': 15, 'Y_DAN': 57}, {'FASES': 3, 'CABO': 70, 'VAO_M': 20, 'Y_DAN': 100},
    {'FASES': 3, 'CABO': 70, 'VAO_M': 25, 'Y_DAN': 156}, {'FASES': 3, 'CABO': 70, 'VAO_M': 30, 'Y_DAN': 224},
    {'FASES': 3, 'CABO': 70, 'VAO_M': 35, 'Y_DAN': 305}, {'FASES': 3, 'CABO': 70, 'VAO_M': 40, 'Y_DAN': 398},
    {'FASES': 3, 'CABO': 35, 'VAO_M': 5, 'Y_DAN': 4}, {'FASES': 3, 'CABO': 35, 'VAO_M': 10, 'Y_DAN': 16},
    {'FASES': 3, 'CABO': 35, 'VAO_M': 15, 'Y_DAN': 34}, {'FASES': 3, 'CABO': 35, 'VAO_M': 20, 'Y_DAN': 57},
    {'FASES': 3, 'CABO': 35, 'VAO_M': 25, 'Y_DAN': 88}, {'FASES': 3, 'CABO': 35, 'VAO_M': 30, 'Y_DAN': 126},
    {'FASES': 3, 'CABO': 35, 'VAO_M': 35, 'Y_DAN': 172}, {'FASES': 3, 'CABO': 35, 'VAO_M': 40, 'Y_DAN': 225},
    {'FASES': 3, 'CABO': 35, 'VAO_M': 45, 'Y_DAN': 285}, {'FASES': 3, 'CABO': 35, 'VAO_M': 50, 'Y_DAN': 303},
    {'FASES': 3, 'CABO': 35, 'VAO_M': 55, 'Y_DAN': 350}, {'FASES': 3, 'CABO': 35, 'VAO_M': 60, 'Y_DAN': 400},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 5, 'Y_DAN': 1}, {'FASES': 1, 'CABO': 25, 'VAO_M': 10, 'Y_DAN': 5},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 15, 'Y_DAN': 12}, {'FASES': 1, 'CABO': 25, 'VAO_M': 20, 'Y_DAN': 21},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 25, 'Y_DAN': 32}, {'FASES': 1, 'CABO': 25, 'VAO_M': 30, 'Y_DAN': 47},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 35, 'Y_DAN': 64}, {'FASES': 1, 'CABO': 25, 'VAO_M': 40, 'Y_DAN': 83},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 45, 'Y_DAN': 101}, {'FASES': 1, 'CABO': 25, 'VAO_M': 50, 'Y_DAN': 125},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 55, 'Y_DAN': 151}, {'FASES': 1, 'CABO': 25, 'VAO_M': 60, 'Y_DAN': 180},
]

DB_COMPACTA = [
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 15, 'Y_DAN': 342}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 20, 'Y_DAN': 349},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 25, 'Y_DAN': 355}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 30, 'Y_DAN': 365},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 35, 'Y_DAN': 386}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 40, 'Y_DAN': 405},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 45, 'Y_DAN': 422}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 50, 'Y_DAN': 438},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 55, 'Y_DAN': 451}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 60, 'Y_DAN': 464},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 65, 'Y_DAN': 475}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 70, 'Y_DAN': 485},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 75, 'Y_DAN': 494}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 80, 'Y_DAN': 503},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 85, 'Y_DAN': 510}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 90, 'Y_DAN': 517},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 95, 'Y_DAN': 523}, {'TENSAO': 15, 'FASES': 3, 'CABO': 35, 'VAO_M': 100, 'Y_DAN': 529},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 15, 'Y_DAN': 366}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 20, 'Y_DAN': 383},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 25, 'Y_DAN': 400}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 30, 'Y_DAN': 417},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 35, 'Y_DAN': 444}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 40, 'Y_DAN': 468},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 45, 'Y_DAN': 490}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 50, 'Y_DAN': 511},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 55, 'Y_DAN': 529}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 60, 'Y_DAN': 546},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 65, 'Y_DAN': 561}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 70, 'Y_DAN': 575},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 75, 'Y_DAN': 588}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 80, 'Y_DAN': 599},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 85, 'Y_DAN': 610}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 90, 'Y_DAN': 620},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 95, 'Y_DAN': 629}, {'TENSAO': 15, 'FASES': 3, 'CABO': 70, 'VAO_M': 100, 'Y_DAN': 637},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 15, 'Y_DAN': 442}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 20, 'Y_DAN': 487},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 25, 'Y_DAN': 528}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 30, 'Y_DAN': 567},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 35, 'Y_DAN': 603}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 40, 'Y_DAN': 643},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 45, 'Y_DAN': 680}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 50, 'Y_DAN': 714},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 55, 'Y_DAN': 746}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 60, 'Y_DAN': 775},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 65, 'Y_DAN': 802}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 70, 'Y_DAN': 827},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 75, 'Y_DAN': 850}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 80, 'Y_DAN': 872},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 85, 'Y_DAN': 892}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 90, 'Y_DAN': 911},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 95, 'Y_DAN': 929}, {'TENSAO': 15, 'FASES': 3, 'CABO': 185, 'VAO_M': 100, 'Y_DAN': 945},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 15, 'Y_DAN': 478}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 20, 'Y_DAN': 533},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 25, 'Y_DAN': 584}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 30, 'Y_DAN': 631},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 35, 'Y_DAN': 674}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 40, 'Y_DAN': 720},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 45, 'Y_DAN': 763}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 50, 'Y_DAN': 803},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 55, 'Y_DAN': 840}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 60, 'Y_DAN': 875},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 65, 'Y_DAN': 907}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 70, 'Y_DAN': 937},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 75, 'Y_DAN': 966}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 80, 'Y_DAN': 992},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 85, 'Y_DAN': 1017}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 90, 'Y_DAN': 1040},
    {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 95, 'Y_DAN': 1062}, {'TENSAO': 15, 'FASES': 3, 'CABO': 240, 'VAO_M': 100, 'Y_DAN': 1082},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 15, 'Y_DAN': 433}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 20, 'Y_DAN': 475},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 25, 'Y_DAN': 514}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 30, 'Y_DAN': 557},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 35, 'Y_DAN': 600}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 40, 'Y_DAN': 640},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 45, 'Y_DAN': 676}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 50, 'Y_DAN': 710},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 55, 'Y_DAN': 741}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 60, 'Y_DAN': 770},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 65, 'Y_DAN': 797}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 70, 'Y_DAN': 822},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 75, 'Y_DAN': 845}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 80, 'Y_DAN': 867},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 85, 'Y_DAN': 887}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 90, 'Y_DAN': 905},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 95, 'Y_DAN': 923}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 70, 'VAO_M': 100, 'Y_DAN': 939},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 15, 'Y_DAN': 521}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 20, 'Y_DAN': 588},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 25, 'Y_DAN': 650}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 30, 'Y_DAN': 707},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 35, 'Y_DAN': 767}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 40, 'Y_DAN': 822},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 45, 'Y_DAN': 874}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 50, 'Y_DAN': 922},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 55, 'Y_DAN': 966}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 60, 'Y_DAN': 1008},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 65, 'Y_DAN': 1048}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 70, 'Y_DAN': 1085},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 75, 'Y_DAN': 1119}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 80, 'Y_DAN': 1152},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 85, 'Y_DAN': 1183}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 90, 'Y_DAN': 1212},
    {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 95, 'Y_DAN': 1239}, {'TENSAO': 36.2, 'FASES': 3, 'CABO': 185, 'VAO_M': 100, 'Y_DAN': 1265},
]

DB_ILUMINACAO = [
    {'FASES': 1, 'CABO': 16, 'VAO_M': 5, 'Y_DAN': 5}, {'FASES': 1, 'CABO': 16, 'VAO_M': 10, 'Y_DAN': 16},
    {'FASES': 1, 'CABO': 16, 'VAO_M': 15, 'Y_DAN': 31}, {'FASES': 1, 'CABO': 16, 'VAO_M': 20, 'Y_DAN': 46},
    {'FASES': 1, 'CABO': 16, 'VAO_M': 25, 'Y_DAN': 61}, {'FASES': 1, 'CABO': 16, 'VAO_M': 30, 'Y_DAN': 77},
    {'FASES': 1, 'CABO': 16, 'VAO_M': 35, 'Y_DAN': 83}, {'FASES': 1, 'CABO': 16, 'VAO_M': 40, 'Y_DAN': 84},
    {'FASES': 1, 'CABO': 16, 'VAO_M': 45, 'Y_DAN': 85}, {'FASES': 1, 'CABO': 16, 'VAO_M': 50, 'Y_DAN': 86},
    {'FASES': 1, 'CABO': 16, 'VAO_M': 55, 'Y_DAN': 86}, {'FASES': 1, 'CABO': 16, 'VAO_M': 60, 'Y_DAN': 87},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 5, 'Y_DAN': 1}, {'FASES': 1, 'CABO': 25, 'VAO_M': 10, 'Y_DAN': 5},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 15, 'Y_DAN': 12}, {'FASES': 1, 'CABO': 25, 'VAO_M': 20, 'Y_DAN': 21},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 25, 'Y_DAN': 32}, {'FASES': 1, 'CABO': 25, 'VAO_M': 30, 'Y_DAN': 47},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 35, 'Y_DAN': 64}, {'FASES': 1, 'CABO': 25, 'VAO_M': 40, 'Y_DAN': 83},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 45, 'Y_DAN': 101}, {'FASES': 1, 'CABO': 25, 'VAO_M': 50, 'Y_DAN': 125},
    {'FASES': 1, 'CABO': 25, 'VAO_M': 55, 'Y_DAN': 151}, {'FASES': 1, 'CABO': 25, 'VAO_M': 60, 'Y_DAN': 180},
    {'FASES': 2, 'CABO': 16, 'VAO_M': 5, 'Y_DAN': 6}, {'FASES': 2, 'CABO': 16, 'VAO_M': 10, 'Y_DAN': 21},
    {'FASES': 2, 'CABO': 16, 'VAO_M': 15, 'Y_DAN': 40}, {'FASES': 2, 'CABO': 16, 'VAO_M': 20, 'Y_DAN': 60},
    {'FASES': 2, 'CABO': 16, 'VAO_M': 25, 'Y_DAN': 79}, {'FASES': 2, 'CABO': 16, 'VAO_M': 30, 'Y_DAN': 84},
    {'FASES': 2, 'CABO': 16, 'VAO_M': 35, 'Y_DAN': 85}, {'FASES': 2, 'CABO': 16, 'VAO_M': 40, 'Y_DAN': 86},
    {'FASES': 2, 'CABO': 16, 'VAO_M': 45, 'Y_DAN': 87}, {'FASES': 2, 'CABO': 16, 'VAO_M': 50, 'Y_DAN': 87},
    {'FASES': 2, 'CABO': 16, 'VAO_M': 55, 'Y_DAN': 88}, {'FASES': 2, 'CABO': 16, 'VAO_M': 60, 'Y_DAN': 88},
    {'FASES': 2, 'CABO': 25, 'VAO_M': 5, 'Y_DAN': 7}, {'FASES': 2, 'CABO': 25, 'VAO_M': 10, 'Y_DAN': 27},
    {'FASES': 2, 'CABO': 25, 'VAO_M': 15, 'Y_DAN': 52}, {'FASES': 2, 'CABO': 25, 'VAO_M': 20, 'Y_DAN': 78},
    {'FASES': 2, 'CABO': 25, 'VAO_M': 25, 'Y_DAN': 107}, {'FASES': 2, 'CABO': 25, 'VAO_M': 30, 'Y_DAN': 138},
    {'FASES': 2, 'CABO': 25, 'VAO_M': 35, 'Y_DAN': 128}, {'FASES': 2, 'CABO': 25, 'VAO_M': 40, 'Y_DAN': 130},
    {'FASES': 2, 'CABO': 25, 'VAO_M': 45, 'Y_DAN': 131}, {'FASES': 2, 'CABO': 25, 'VAO_M': 50, 'Y_DAN': 132},
    {'FASES': 2, 'CABO': 25, 'VAO_M': 55, 'Y_DAN': 133}, {'FASES': 2, 'CABO': 25, 'VAO_M': 60, 'Y_DAN': 134},
    {'FASES': 3, 'CABO': 16, 'VAO_M': 5, 'Y_DAN': 7}, {'FASES': 3, 'CABO': 16, 'VAO_M': 10, 'Y_DAN': 25},
    {'FASES': 3, 'CABO': 16, 'VAO_M': 15, 'Y_DAN': 47}, {'FASES': 3, 'CABO': 16, 'VAO_M': 20, 'Y_DAN': 70},
    {'FASES': 3, 'CABO': 16, 'VAO_M': 25, 'Y_DAN': 84}, {'FASES': 3, 'CABO': 16, 'VAO_M': 30, 'Y_DAN': 86},
    {'FASES': 3, 'CABO': 16, 'VAO_M': 35, 'Y_DAN': 85}, {'FASES': 3, 'CABO': 16, 'VAO_M': 40, 'Y_DAN': 87},
    {'FASES': 3, 'CABO': 16, 'VAO_M': 45, 'Y_DAN': 87}, {'FASES': 3, 'CABO': 16, 'VAO_M': 50, 'Y_DAN': 88},
    {'FASES': 3, 'CABO': 16, 'VAO_M': 55, 'Y_DAN': 88}, {'FASES': 3, 'CABO': 16, 'VAO_M': 60, 'Y_DAN': 88},
    {'FASES': 3, 'CABO': 25, 'VAO_M': 5, 'Y_DAN': 9}, {'FASES': 3, 'CABO': 25, 'VAO_M': 10, 'Y_DAN': 32},
    {'FASES': 3, 'CABO': 25, 'VAO_M': 15, 'Y_DAN': 61}, {'FASES': 3, 'CABO': 25, 'VAO_M': 20, 'Y_DAN': 93},
    {'FASES': 3, 'CABO': 25, 'VAO_M': 25, 'Y_DAN': 129}, {'FASES': 3, 'CABO': 25, 'VAO_M': 30, 'Y_DAN': 128},
    {'FASES': 3, 'CABO': 25, 'VAO_M': 35, 'Y_DAN': 130}, {'FASES': 3, 'CABO': 25, 'VAO_M': 40, 'Y_DAN': 132},
    {'FASES': 3, 'CABO': 25, 'VAO_M': 45, 'Y_DAN': 133}, {'FASES': 3, 'CABO': 25, 'VAO_M': 50, 'Y_DAN': 133},
    {'FASES': 3, 'CABO': 25, 'VAO_M': 55, 'Y_DAN': 134}, {'FASES': 3, 'CABO': 25, 'VAO_M': 60, 'Y_DAN': 135},
]

DB_POSTES = [
    # Apenas postes com 400 daN ou mais
    {'Resistencia_daN': 400, 'Codificacao': '9400', 'Altura_m': 9},
    {'Resistencia_daN': 400, 'Codificacao': '12400', 'Altura_m': 12},
    {'Resistencia_daN': 600, 'Codificacao': '11600', 'Altura_m': 11},
    {'Resistencia_daN': 600, 'Codificacao': '12600', 'Altura_m': 12},
    {'Resistencia_daN': 1000, 'Codificacao': '111000', 'Altura_m': 11},
    {'Resistencia_daN': 1000, 'Codificacao': '121000', 'Altura_m': 12},
    {'Resistencia_daN': 1500, 'Codificacao': '121500', 'Altura_m': 12},
    {'Resistencia_daN': 1500, 'Codificacao': '141500', 'Altura_m': 14},
    {'Resistencia_daN': 1500, 'Codificacao': '161500', 'Altura_m': 16},
]

TODOS_OS_CABOS = {
    'COMPACTA': DB_COMPACTA,
    'SECUNDARIA': DB_SECUNDARIA,
    'ILUMINACAO PUBLICA': DB_ILUMINACAO
}

def get_options(db, filter_key=None, filter_value=None):
    if filter_key and filter_value is not None:
        return sorted(list(set(c['CABO'] for c in db if c.get(filter_key) == filter_value)))
    return sorted(list(set(c[list(c.keys())[0]] for c in db)))

def find_effort(db, vao_usuario, cabo_selecionado, **kwargs):
    opcoes_cabo_filtrado = [c for c in db if c['CABO'] == cabo_selecionado and all(c.get(k) == v for k, v in kwargs.items())]
    
    opcoes_vao_validas = [c for c in opcoes_cabo_filtrado if c['VAO_M'] >= vao_usuario]
    
    if not opcoes_vao_validas:
        return None, None 
        
    linha_selecionada = min(opcoes_vao_validas, key=lambda x: x['VAO_M'])
    return linha_selecionada['Y_DAN'], linha_selecionada['VAO_M']

def recomendar_poste(esforco_requerido, tem_compacta):
    esforco_final_para_busca = max(esforco_requerido, 400)
    
    postes_disponiveis = DB_POSTES
    if tem_compacta:
        postes_filtrados_altura = [p for p in postes_disponiveis if p['Altura_m'] >= 12]
    else:
        postes_filtrados_altura = [p for p in postes_disponiveis if p['Altura_m'] >= 9]

    postes_adequados = [p for p in postes_filtrados_altura if p['Resistencia_daN'] >= esforco_final_para_busca]
    if not postes_adequados:
        return f"Nenhum poste com altura requerida suporta {esforco_final_para_busca:.2f} daN."
    
    poste_recomendado = min(postes_adequados, key=lambda x: x['Resistencia_daN'])
    return f"{poste_recomendado['Codificacao']} ({poste_recomendado['Resistencia_daN']} daN)"

def plotar_e_salvar_grafico(direcoes, nome_poste):
    fig, ax = plt.subplots(figsize=(8, 8))
    cores = ['#007bff', '#28a745', '#dc3545', '#17a2b8', '#ffc107', '#6f42c1']
    
    rx_total, ry_total = 0, 0
    vetores_para_plotar = []

    for direcao in direcoes:
        esforco = direcao['esforco_total']
        angulo_rad = np.deg2rad(direcao['angulo'])
        fx, fy = esforco * np.cos(angulo_rad), esforco * np.sin(angulo_rad)
        vetores_para_plotar.append({'label': f"Dir. {direcao['id']} ({esforco:.0f} daN)", 'fx': fx, 'fy': fy})
        rx_total += fx
        ry_total += fy

    resultante_mag = np.sqrt(rx_total**2 + ry_total**2)
    resultante_angulo = np.rad2deg(np.arctan2(ry_total, rx_total)) % 360
    vetor_resultante = {'label': f'Resultante ({resultante_mag:.0f} daN)', 'fx': rx_total, 'fy': ry_total}

    for i, vetor in enumerate(vetores_para_plotar):
        ax.quiver(0, 0, vetor['fx'], vetor['fy'], angles='xy', scale_units='xy', scale=1, color=cores[i % len(cores)], label=vetor['label'], width=0.003)
    ax.quiver(0, 0, vetor_resultante['fx'], vetor_resultante['fy'], angles='xy', scale_units='xy', scale=1, color='k', width=0.006, label=vetor_resultante['label'])
    
    ax.set_title(f"Diagrama Vetorial - Poste '{nome_poste}'", fontsize=16)
    ax.set_xlabel('Componente X (daN)', fontsize=12)
    ax.set_ylabel('Componente Y (daN)', fontsize=12)
    ax.axhline(0, color='grey', lw=0.5); ax.axvline(0, color='grey', lw=0.5)
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.legend()
    ax.set_aspect('equal', adjustable='box')
    
    buf = BytesIO()
    fig.savefig(buf, format="png", dpi=150)
    plt.close(fig)
    return resultante_mag, resultante_angulo, buf

def obter_parametros_cabo(nome_tipo, i, j, k):
    db = TODOS_OS_CABOS[nome_tipo]
    
    if nome_tipo == 'COMPACTA':
        opcoes_tensao = sorted(list(set(c['TENSAO'] for c in db)))
        tensao_sel = st.selectbox("Tensão:", opcoes_tensao, key=f"tensao_{i}_{j}_{k}")
        db_filtrado = [c for c in db if c['TENSAO'] == tensao_sel]
        opcoes_cabo = sorted(list(set(c['CABO'] for c in db_filtrado)))
        cabo_sel = st.selectbox("Cabo (bitola):", opcoes_cabo, key=f"cabo_{i}_{j}_{k}")
        vao_sel = st.number_input("Vão (m):", min_value=1, step=1, key=f"vao_{i}_{j}_{k}")
        esforco, vao_usado = find_effort(db, vao_sel, cabo_sel, TENSAO=tensao_sel)

    else: 
        opcoes_fases = sorted(list(set(c['FASES'] for c in db)))
        fases_sel = st.selectbox("Fases:", opcoes_fases, key=f"fases_{i}_{j}_{k}")
        db_filtrado = [c for c in db if c['FASES'] == fases_sel]
        opcoes_cabo = sorted(list(set(c['CABO'] for c in db_filtrado)))
        cabo_sel = st.selectbox("Cabo (bitola):", opcoes_cabo, key=f"cabo_{i}_{j}_{k}")
        vao_sel = st.number_input("Vão (m):", min_value=1, step=1, key=f"vao_{i}_{j}_{k}")
        esforco, vao_usado = find_effort(db, vao_sel, cabo_sel, FASES=fases_sel)

    if esforco is not None:
        st.info(f"Vão para cálculo: {vao_usado}m -> Esforço: {esforco} daN")
        return {'esforco': esforco, 'tipo': nome_tipo}
    else:
        st.warning(f"Combinação não encontrada ou vão acima do limite para {nome_tipo} {cabo_sel}mm².")
        return None

def main_app():
    st.set_page_config(layout="wide", page_title="Calculadora de Esforços em Poste")
    st.title("⚙️ Calculadora de Esforços em Poste")

    if 'page' not in st.session_state:
        st.session_state.page = 'input'
        st.session_state.all_postes_data = []

    if st.session_state.page == 'input':
        with st.form("form_projeto"):
            st.subheader("Configuração do Projeto")
            num_postes = st.number_input("Quantidade de postes a serem calculados:", min_value=1, value=1, step=1)
            
            postes_form_data = []
            for i in range(num_postes):
                st.markdown(f"---")
                st.markdown(f"### **Poste {i+1}**")
                nome_poste = st.text_input("Nome/Identificador do Poste:", key=f"nome_poste_{i}")
                num_direcoes = st.number_input("Número de direções de esforço para este poste:", min_value=1, value=1, step=1, key=f"num_dir_{i}")
                
                direcoes_form_data = []
                for j in range(num_direcoes):
                    cols = st.columns([1, 2])
                    with cols[0]:
                        st.markdown(f"**Direção {j+1}**")
                        angulo = st.number_input(f"Ângulo (0-360°):", min_value=0.0, max_value=360.0, value=0.0, step=1.0, key=f"angulo_{i}_{j}")
                    
                    with cols[1]:
                        tipos_de_cabo_str = st.multiselect(
                            "Selecione os tipos de cabo nesta direção:",
                            options=['COMPACTA', 'SECUNDARIA', 'ILUMINACAO PUBLICA'],
                            key=f"tipos_{i}_{j}"
                        )
                    direcoes_form_data.append({'angulo': angulo, 'tipos_selecionados': tipos_de_cabo_str})
                postes_form_data.append({'nome_poste': nome_poste, 'direcoes': direcoes_form_data})

            submitted = st.form_submit_button("Avançar para Detalhar Cabos")

            if submitted:
                st.session_state.postes_form_data = postes_form_data
                st.session_state.page = 'details'
                st.rerun()
    
    elif st.session_state.page == 'details':
        st.header("Detalhes dos Cabos")
        all_postes_data = []
        
        with st.form("form_details"):
            for i, poste_data in enumerate(st.session_state.postes_form_data):
                st.subheader(f"Poste: {poste_data['nome_poste']}")
                direcoes_calculadas = []
                tem_compacta_poste = False

                for j, direcao_data in enumerate(poste_data['direcoes']):
                    st.markdown(f"**Direção {j+1} (Ângulo {direcao_data['angulo']}°)**")
                    esforco_total_direcao = 0
                    
                    for k, tipo in enumerate(direcao_data['tipos_selecionados']):
                        with st.expander(f"Dados para cabo {tipo} na Direção {j+1}"):
                            resultado = obter_parametros_cabo(tipo, i, j, k)
                            if resultado:
                                esforco_total_direcao += resultado['esforco']
                                if resultado['tipo'] == 'COMPACTA':
                                    tem_compacta_poste = True
                    
                    direcoes_calculadas.append({'id': str(j + 1), 'angulo': direcao_data['angulo'], 'esforco_total': esforco_total_direcao})

                all_postes_data.append({'nome_poste': poste_data['nome_poste'], 'direcoes': direcoes_calculadas, 'tem_compacta': tem_compacta_poste})

            submitted_details = st.form_submit_button("Calcular Resultados Finais")

            if submitted_details:
                st.session_state.all_postes_data = all_postes_data
                st.session_state.page = 'results'
                st.rerun()

    elif st.session_state.page == 'results':
        st.header("Resultados do Projeto")
        resultados_finais_para_excel = []

        for i, poste_data in enumerate(st.session_state.all_postes_data):
            nome_poste = poste_data['nome_poste']
            st.markdown(f"---")
            st.subheader(f"Resultados para o Poste: '{nome_poste}'")
            
            resultante_mag, resultante_angulo, grafico_buffer = plotar_e_salvar_grafico(poste_data['direcoes'], nome_poste)
            
            poste_rec = "Nenhum esforço aplicado."
            if resultante_mag > 0:
                poste_rec = recomendar_poste(resultante_mag, poste_data['tem_compacta'])

            col1, col2 = st.columns(2)
            with col1:
                st.metric(label="Força Resultante Calculada", value=f"{resultante_mag:.2f} daN")
                st.metric(label="Ângulo da Resultante", value=f"{resultante_angulo:.2f}°")
                st.success(f"**Poste Recomendado:** {poste_rec}")
            with col2:
                st.image(grafico_buffer, caption=f"Diagrama Vetorial para '{nome_poste}'")
                st.download_button(
                    label=f"Baixar Gráfico de '{nome_poste}'",
                    data=grafico_buffer,
                    file_name=f"grafico_{nome_poste.replace(' ', '_')}.png",
                    mime="image/png",
                    key=f"download_button_{i}" # Chave única para o botão de download
                )

            relatorio_poste = {'ID do Poste': nome_poste}
            for j, direcao in enumerate(poste_data['direcoes']):
                relatorio_poste[f'Esforço Direção {j+1} (daN)'] = f"{direcao['esforco_total']:.2f}"
                relatorio_poste[f'Ângulo Direção {j+1} (°)'] = f"{direcao['angulo']:.1f}"
            
            relatorio_poste['Resultante Final (daN)'] = f"{resultante_mag:.2f}"
            relatorio_poste['Ângulo da Resultante (°)'] = f"{resultante_angulo:.1f}"
            relatorio_poste['Poste Recomendado'] = poste_rec
            resultados_finais_para_excel.append(relatorio_poste)
            
        st.markdown("---")
        st.header("Relatório Final do Projeto")
        df_resultados = pd.DataFrame(resultados_finais_para_excel)
        st.dataframe(df_resultados)
        
        output = BytesIO()
        with pd.ExcelWriter(output, engine='openpyxl') as writer:
            df_resultados.to_excel(writer, index=False, sheet_name='Relatorio')
        processed_data = output.getvalue()

        st.download_button(
            label="📥 Baixar Relatório Completo em Excel",
            data=processed_data,
            file_name="relatorio_esforcos_postes.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )

        if st.button("Iniciar Novo Cálculo"):
            st.session_state.page = 'input'
            st.session_state.pop('postes_form_data', None)
            st.session_state.pop('all_postes_data', None)
            st.session_state.pop('resultados_finais', None)
            st.rerun()

if __name__ == "__main__":
    main_app()
