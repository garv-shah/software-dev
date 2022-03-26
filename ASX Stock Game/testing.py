
from tradingview_ta import Interval, get_multiple_analysis
import matplotlib.pyplot as plt

symbol_list = [
    "360",
    "A2M",
    "AAA",
    "AAC",
    "ABB",
    "ABC",
    "ABP",
    "ACDC",
    "AD8",
    "ADH",
    "ADT",
    "AEF",
    "AFG",
    "AFI",
    "AGG",
    "AGL",
    "AIA",
    "AIZ",
    "AKE",
    "AKP",
    "ALG",
    "ALL",
    "ALQ",
    "ALU",
    "ALX",
    "AMC",
    "ANN",
    "ANZ",
    "APA",
    "APE",
    "APX",
    "AQZ",
    "ARB",
    "ARF",
    "ARG",
    "ASB",
    "ASIA",
    "ASM",
    "ASX",
    "ATEC",
    "AUB",
    "AWC",
    "AX1",
    "AZJ",
    "BAP",
    "BBN",
    "BEAR",
    "BEN",
    "BGA",
    "BHP",
    "BKL",
    "BKW",
    "BLD",
    "BLX",
    "BOQ",
    "BPT",
    "BRG",
    "BRN",
    "BSL",
    "BVS",
    "BWP",
    "BWX",
    "BXB",
    "CAR",
    "CBA",
    "CCP",
    "CCX",
    "CDA",
    "CEN",
    "CGC",
    "CGF",
    "CHC",
    "CHN",
    "CIA",
    "CIP",
    "CKF",
    "CLDD",
    "CLNE",
    "CLW",
    "CMM",
    "CNEW",
    "CNI",
    "CNU",
    "COF",
    "COH",
    "COL",
    "CPU",
    "CQE",
    "CQR",
    "CRN",
    "CRYP",
    "CSL",
    "CSR",
    "CTD",
    "CTT",
    "CUV",
    "CWP",
    "CWY",
    "DBI",
    "DDR",
    "DEG",
    "DHG",
    "DMP",
    "DOW",
    "DRIV",
    "DRR",
    "DTL",
    "DUB",
    "DXI",
    "DXS",
    "EBO",
    "ECX",
    "EDV",
    "EHE",
    "EML",
    "EOS",
    "ERTH",
    "ESPO",
    "ETHI",
    "EVN",
    "EVT",
    "F100",
    "FAIR",
    "FANG",
    "FBU",
    "FCL",
    "FDV",
    "FLT",
    "FMG",
    "FPH",
    "FUEL",
    "GDX",
    "GEAR",
    "GEM",
    "GMA",
    "GMG",
    "GNC",
    "GOLD",
    "GOR",
    "GOZ",
    "GPT",
    "GUD",
    "GWA",
    "HACK",
    "HBRD",
    "HDN",
    "HGEN",
    "HLS",
    "HM1",
    "HMC",
    "HPI",
    "HSN",
    "HT1",
    "HUB",
    "HVN",
    "IAF",
    "IAG",
    "IDX",
    "IEL",
    "IEM",
    "IEU",
    "IFL",
    "IFM",
    "IFRA",
    "IGO",
    "ILU",
    "IMD",
    "IMPQ",
    "INA",
    "ING",
    "IPH",
    "IPL",
    "IRE",
    "IVC",
    "IVV",
    "IXJ",
    "JBH",
    "JHG",
    "JHX",
    "JIN",
    "JLG",
    "KAR",
    "KGN",
    "KLS",
    "KMD",
    "LFG",
    "LIC",
    "LLC",
    "LOV",
    "LSF",
    "LTR",
    "LYC",
    "MAF",
    "MAQ",
    "MCR",
    "MEZ",
    "MGH",
    "MGR",
    "MKAX",
    "MMS",
    "MND",
    "MNY",
    "MP1",
    "MPL",
    "MQG",
    "MSB",
    "MTS",
    "MVW",
    "MYS",
    "NAB",
    "NAN",
    "NCK",
    "NCM",
    "NDQ",
    "NEA",
    "NEC",
    "NHC",
    "NHF",
    "NSR",
    "NST",
    "NUF",
    "NVX",
    "NWH",
    "NWL",
    "NWS",
    "NXL",
    "NXT",
    "OBL",
    "OCL",
    "OFX",
    "OML",
    "OOO",
    "OPT",
    "ORA",
    "ORG",
    "ORI",
    "OZF",
    "OZL",
    "PAR",
    "PBH",
    "PDL",
    "PGH",
    "PIXX",
    "PLS",
    "PME",
    "PMV",
    "PNI",
    "PNV",
    "PPH",
    "PPK",
    "PPS",
    "PPT",
    "PRU",
    "PSI",
    "PTM",
    "PWH",
    "QAN",
    "QBE",
    "QRE",
    "QSML",
    "QUAL",
    "QUB",
    "RBL",
    "RDV",
    "REA",
    "REG",
    "REH",
    "RFF",
    "RHC",
    "RIO",
    "RMC",
    "RMD",
    "RMS",
    "ROBO",
    "RRL",
    "RWC",
    "S32",
    "SBM",
    "SCG",
    "SCP",
    "SDF",
    "SEK",
    "SEMI",
    "SFR",
    "SGF",
    "SGM",
    "SGP",
    "SGR",
    "SHL",
    "SHV",
    "SIQ",
    "SKC",
    "SLF",
    "SLR",
    "SM1",
    "SNAS",
    "SOL",
    "SPK",
    "SPL",
    "SQ2",
    "SSR",
    "STO",
    "STW",
    "SUL",
    "SUN",
    "SVW",
    "SXL",
    "SYR",
    "TAH",
    "TCL",
    "TECH",
    "TGR",
    "TLS",
    "TLX",
    "TNE",
    "TPG",
    "TPW",
    "TUA",
    "TWE",
    "UMG",
    "URW",
    "UWL",
    "VAP",
    "VAS",
    "VCX",
    "VDHG",
    "VEA",
    "VGAD",
    "VGS",
    "VHY",
    "VSO",
    "VUK",
    "VUL",
    "VVLU",
    "WAF",
    "WAM",
    "WBC",
    "WEB",
    "WES",
    "WHC",
    "WOR",
    "WOW",
    "WPL",
    "WPR",
    "WTC",
    "WXOZ",
    "XRO",
    "YAL",
    "Z1P",
    "ZIM"
]


def main():
    output_list = []
    output_dict = {}

    analysis = get_multiple_analysis(
        screener="australia",
        interval=Interval.INTERVAL_1_HOUR,
        symbols=["asx:" + symbol for symbol in symbol_list]
    )

    for key in analysis.keys():
        if analysis[key].summary['RECOMMENDATION'] == 'STRONG_BUY':
            print(key.split(':')[1])

    # for symbol in symbol_list:
    #     print(symbol)
    #     output = TA_Handler(
    #         symbol=symbol,
    #         screener="australia",
    #         exchange="ASX",
    #         interval=Interval.INTERVAL_1_DAY
    #     )
    #
    #     summary = output.get_analysis().summary
    #
    #     output_list.append([symbol, summary])
    #     if summary['RECOMMENDATION'] == 'STRONG_BUY':
    #         output_dict[symbol] = summary
    #
    # print(output_dict)
    #
    # with open("./data/ASX_Stock_Game_Data.csv", 'w+', newline='') as csvfile:
    #     fieldnames = list(output_dict.keys())
    #     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #     writer.writeheader()
    #     writer.writerow(output_dict)
    #     csvfile.close()
    #
    # keys = list(output_dict.keys())
    # vals = [float(output_dict[k]['BUY']) for k in keys]
    # plt.style.use('seaborn-dark')
    # plt.figure(figsize=(18, 5))
    # sns.barplot(x=keys, y=vals)
    # plt.xlabel('\nSymbol')
    # plt.ylabel('Buy Intensity')
    # plt.title('Daily NOVA Stock Advice')
    # plt.grid()
    # plt.savefig('./NOVA_Stock_Advice.png')


if __name__ == "__main__":
    main()
