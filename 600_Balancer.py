import io
import string
import math

#list of Pokemon and their evolutionary stage and legendary status, by gen

#Gen IV globals

#data skip
data_skip_4 = 117


pokemon_gen_4 = [[0,0],[1,2],[2,1],[3,0],[4,2],[5,1],[6,0],[7,2],[8,1],[9,0],[10,2],[11,1],[12,0],[13,2],[14,1],[15,0],[16,2],[17,1],[18,0],[19,1],[20,0],[21,1],[22,0],[23,1],[24,0],[25,1],[26,0],[27,1],[28,0],[29,2],[30,1],[31,0],[32,2],[33,1],[34,0],[35,1],[36,0],[37,1],[38,0],[39,1],[40,0],[41,2],[42,1],[43,2],[44,1],[45,0],[46,1],[47,0],[48,1],[49,0],[50,1],[51,0],[52,1],[53,0],[54,1],[55,0],[56,1],[57,0],[58,1],[59,0],[60,2],[61,1],[62,0],[63,2],[64,1],[65,0],[66,2],[67,1],[68,0],[69,2],[70,1],[71,0],[72,1],[73,0],[74,2],[75,1],[76,0],[77,1],[78,0],[79,1],[80,0],[81,2],[82,1],[83,0],[84,1],[85,0],[86,1],[87,0],[88,1],[89,0],[90,1],[91,0],[92,2],[93,1],[94,0],[95,1],[96,1],[97,0],[98,1],[99,0],[100,1],[101,0],[102,1],[103,0],[104,1],[105,0],[106,0],[107,0],[108,1],[109,1],[110,0],[111,2],[112,1],[113,1],[114,1],[115,0],[116,2],[117,1],[118,1],[119,0],[120,1],[121,0],[122,0],[123,0],[124,0],[125,1],[126,1],[127,0],[128,0],[129,1],[130,0],[131,0],[132,0],[133,1],[134,0],[135,0],[136,0],[137,2],[138,1],[139,0],[140,1],[141,0],[142,0],[143,0],[144,5],[145,5],[146,5],[147,2],[148,1],[149,0],[150,4],[151,4],[152,2],[153,1],[154,0],[155,2],[156,1],[157,0],[158,2],[159,1],[160,0],[161,1],[162,0],[163,1],[164,0],[165,1],[166,0],[167,1],[168,0],[169,0],[170,1],[171,0],[172,2],[173,2],[174,2],[175,2],[176,1],[177,1],[178,0],[179,2],[180,1],[181,0],[182,0],[183,1],[184,0],[185,0],[186,0],[187,2],[188,1],[189,0],[190,1],[191,1],[192,0],[193,1],[194,1],[195,0],[196,0],[197,0],[198,1],[199,0],[200,1],[201,0],[202,0],[203,0],[204,1],[205,0],[206,0],[207,1],[208,0],[209,1],[210,0],[211,0],[212,0],[213,0],[214,0],[215,1],[216,1],[217,0],[218,1],[219,0],[220,2],[221,1],[222,0],[223,1],[224,0],[225,0],[226,0],[227,0],[228,1],[229,0],[230,0],[231,1],[232,0],[233,0],[234,0],[235,0],[236,1],[237,0],[238,1],[239,2],[240,2],[241,0],[242,0],[243,5],[244,5],[245,5],[246,2],[247,1],[248,0],[249,4],[250,4],[251,4],[252,2],[253,1],[254,0],[255,2],[256,1],[257,0],[258,2],[259,1],[260,0],[261,1],[262,0],[263,1],[264,0],[265,2],[266,1],[267,0],[268,1],[269,0],[270,2],[271,1],[272,0],[273,2],[274,1],[275,0],[276,1],[277,0],[278,1],[279,0],[280,2],[281,1],[282,0],[283,1],[284,0],[285,1],[286,0],[287,2],[288,1],[289,0],[290,1],[291,0],[292,0],[293,2],[294,1],[295,0],[296,1],[297,0],[298,2],[299,1],[300,1],[301,0],[302,0],[303,0],[304,2],[305,1],[306,0],[307,1],[308,0],[309,1],[310,0],[311,0],[312,0],[313,0],[314,0],[315,1],[316,1],[317,0],[318,1],[319,0],[320,1],[321,0],[322,1],[323,0],[324,0],[325,1],[326,0],[327,0],[328,2],[329,1],[330,0],[331,1],[332,0],[333,1],[334,0],[335,0],[336,0],[337,0],[338,0],[339,1],[340,0],[341,1],[342,0],[343,1],[344,0],[345,1],[346,0],[347,1],[348,0],[349,1],[350,0],[351,0],[352,0],[353,1],[354,0],[355,1],[356,0],[357,0],[358,0],[359,0],[360,1],[361,1],[362,0],[363,2],[364,1],[365,0],[366,1],[367,0],[368,0],[369,0],[370,0],[371,2],[372,1],[373,0],[374,2],[375,1],[376,0],[377,5],[378,5],[379,5],[380,4],[381,4],[382,4],[383,4],[384,4],[385,4],[386,4],[387,2],[388,1],[389,0],[390,2],[391,1],[392,0],[393,2],[394,1],[395,0],[396,2],[397,1],[398,0],[399,1],[400,0],[401,1],[402,0],[403,2],[404,1],[405,0],[406,2],[407,0],[408,1],[409,0],[410,1],[411,0],[412,1],[413,0],[414,0],[415,1],[416,0],[417,0],[418,1],[419,0],[420,1],[421,0],[422,1],[423,0],[424,0],[425,1],[426,0],[427,1],[428,0],[429,0],[430,0],[431,1],[432,0],[433,1],[434,1],[435,0],[436,1],[437,0],[438,1],[439,1],[440,2],[441,0],[442,0],[443,2],[444,1],[445,0],[446,1],[447,1],[448,0],[449,1],[450,0],[451,1],[452,0],[453,1],[454,0],[455,0],[456,1],[457,0],[458,1],[459,1],[460,0],[461,0],[462,0],[463,0],[464,0],[465,0],[466,0],[467,0],[468,0],[469,0],[470,0],[471,0],[472,0],[473,0],[474,0],[475,0],[476,0],[477,0],[478,0],[479,0],[480,5],[481,5],[482,5],[483,4],[484,4],[485,4],[486,4],[487,4],[488,4],[489,4],[490,4],[491,4],[492,4],[493,4],[494,3],[495,3],[496,4],[497,4],[498,4],[499,0],[500,0],[501,4],[502,4],[503,0],[504,0],[505,0],[506,0],[507,0]]

#Gen VII Globals

data_skip_7 = 237
second_block_7 = 152520

pokemon_gen_7 = [[0,0],[1,2],[2,1],[3,0],[4,2],[5,1],[6,0],[7,2],[8,1],[9,0],[10,2],[11,1],[12,0],[13,2],[14,1],[15,0],[16,2],[17,1],[18,0],[19,1],[20,0],[21,1],[22,0],[23,1],[24,0],[25,1],[26,0],[27,1],[28,0],[29,2],[30,1],[31,0],[32,2],[33,1],[34,0],[35,1],[36,0],[37,1],[38,0],[39,1],[40,0],[41,2],[42,1],[43,2],[44,1],[45,0],[46,1],[47,0],[48,1],[49,0],[50,1],[51,0],[52,1],[53,0],[54,1],[55,0],[56,1],[57,0],[58,1],[59,0],[60,2],[61,1],[62,0],[63,2],[64,1],[65,0],[66,2],[67,1],[68,0],[69,2],[70,1],[71,0],[72,1],[73,0],[74,2],[75,1],[76,0],[77,1],[78,0],[79,1],[80,0],[81,2],[82,1],[83,0],[84,1],[85,0],[86,1],[87,0],[88,1],[89,0],[90,1],[91,0],[92,2],[93,1],[94,0],[95,1],[96,1],[97,0],[98,1],[99,0],[100,1],[101,0],[102,1],[103,0],[104,1],[105,0],[106,0],[107,0],[108,1],[109,1],[110,0],[111,2],[112,1],[113,1],[114,1],[115,0],[116,2],[117,1],[118,1],[119,0],[120,1],[121,0],[122,0],[123,0],[124,0],[125,1],[126,1],[127,0],[128,0],[129,1],[130,0],[131,0],[132,0],[133,1],[134,0],[135,0],[136,0],[137,2],[138,1],[139,0],[140,1],[141,0],[142,0],[143,0],[144,5],[145,5],[146,5],[147,2],[148,1],[149,0],[150,4],[151,4],[152,2],[153,1],[154,0],[155,2],[156,1],[157,0],[158,2],[159,1],[160,0],[161,1],[162,0],[163,1],[164,0],[165,1],[166,0],[167,1],[168,0],[169,0],[170,1],[171,0],[172,2],[173,2],[174,2],[175,2],[176,1],[177,1],[178,0],[179,2],[180,1],[181,0],[182,0],[183,1],[184,0],[185,0],[186,0],[187,2],[188,1],[189,0],[190,1],[191,1],[192,0],[193,1],[194,1],[195,0],[196,0],[197,0],[198,1],[199,0],[200,1],[201,0],[202,0],[203,0],[204,1],[205,0],[206,0],[207,1],[208,0],[209,1],[210,0],[211,0],[212,0],[213,0],[214,0],[215,1],[216,1],[217,0],[218,1],[219,0],[220,2],[221,1],[222,0],[223,1],[224,0],[225,0],[226,0],[227,0],[228,1],[229,0],[230,0],[231,1],[232,0],[233,0],[234,0],[235,0],[236,1],[237,0],[238,1],[239,2],[240,2],[241,0],[242,0],[243,5],[244,5],[245,5],[246,2],[247,1],[248,0],[249,4],[250,4],[251,4],[252,2],[253,1],[254,0],[255,2],[256,1],[257,0],[258,2],[259,1],[260,0],[261,1],[262,0],[263,1],[264,0],[265,2],[266,1],[267,0],[268,1],[269,0],[270,2],[271,1],[272,0],[273,2],[274,1],[275,0],[276,1],[277,0],[278,1],[279,0],[280,2],[281,1],[282,0],[283,1],[284,0],[285,1],[286,0],[287,2],[288,1],[289,0],[290,1],[291,0],[292,0],[293,2],[294,1],[295,0],[296,1],[297,0],[298,2],[299,1],[300,1],[301,0],[302,0],[303,0],[304,2],[305,1],[306,0],[307,1],[308,0],[309,1],[310,0],[311,0],[312,0],[313,0],[314,0],[315,1],[316,1],[317,0],[318,1],[319,0],[320,1],[321,0],[322,1],[323,0],[324,0],[325,1],[326,0],[327,0],[328,2],[329,1],[330,0],[331,1],[332,0],[333,1],[334,0],[335,0],[336,0],[337,0],[338,0],[339,1],[340,0],[341,1],[342,0],[343,1],[344,0],[345,1],[346,0],[347,1],[348,0],[349,1],[350,0],[351,0],[352,0],[353,1],[354,0],[355,1],[356,0],[357,0],[358,0],[359,0],[360,1],[361,1],[362,0],[363,2],[364,1],[365,0],[366,1],[367,0],[368,0],[369,0],[370,0],[371,2],[372,1],[373,0],[374,2],[375,1],[376,0],[377,5],[378,5],[379,5],[380,4],[381,4],[382,4],[383,4],[384,4],[385,4],[386,4],[387,2],[388,1],[389,0],[390,2],[391,1],[392,0],[393,2],[394,1],[395,0],[396,2],[397,1],[398,0],[399,1],[400,0],[401,1],[402,0],[403,2],[404,1],[405,0],[406,2],[407,0],[408,1],[409,0],[410,1],[411,0],[412,1],[413,0],[414,0],[415,1],[416,0],[417,0],[418,1],[419,0],[420,1],[421,0],[422,1],[423,0],[424,0],[425,1],[426,0],[427,1],[428,0],[429,0],[430,0],[431,1],[432,0],[433,1],[434,1],[435,0],[436,1],[437,0],[438,1],[439,1],[440,2],[441,0],[442,0],[443,2],[444,1],[445,0],[446,1],[447,1],[448,0],[449,1],[450,0],[451,1],[452,0],[453,1],[454,0],[455,0],[456,1],[457,0],[458,1],[459,1],[460,0],[461,0],[462,0],[463,0],[464,0],[465,0],[466,0],[467,0],[468,0],[469,0],[470,0],[471,0],[472,0],[473,0],[474,0],[475,0],[476,0],[477,0],[478,0],[479,0],[480,5],[481,5],[482,5],[483,4],[484,4],[485,4],[486,5],[487,4],[488,4],[489,4],[490,4],[491,4],[492,4],[493,4],[494,4],[495,2],[496,1],[497,0],[498,2],[499,1],[500,0],[501,2],[502,1],[503,0],[504,1],[505,0],[506,2],[507,1],[508,0],[509,1],[510,0],[511,1],[512,0],[513,1],[514,0],[515,1],[516,0],[517,1],[518,0],[519,2],[520,1],[521,0],[522,1],[523,0],[524,2],[525,1],[526,0],[527,1],[528,0],[529,1],[530,0],[531,0],[532,2],[533,1],[534,0],[535,2],[536,1],[537,0],[538,0],[539,0],[540,2],[541,1],[542,0],[543,2],[544,1],[545,0],[546,1],[547,0],[548,1],[549,0],[550,0],[551,2],[552,1],[553,0],[554,1],[555,0],[556,0],[557,1],[558,0],[559,1],[560,0],[561,0],[562,1],[563,0],[564,1],[565,0],[566,1],[567,0],[568,1],[569,0],[570,1],[571,0],[572,1],[573,0],[574,2],[575,1],[576,0],[577,2],[578,1],[579,0],[580,1],[581,0],[582,2],[583,1],[584,0],[585,1],[586,0],[587,0],[588,1],[589,0],[590,1],[591,0],[592,1],[593,0],[594,0],[595,1],[596,0],[597,1],[598,0],[599,2],[600,1],[601,0],[602,2],[603,1],[604,0],[605,1],[606,0],[607,2],[608,1],[609,0],[610,2],[611,1],[612,0],[613,1],[614,0],[615,0],[616,1],[617,0],[618,0],[619,1],[620,0],[621,0],[622,1],[623,0],[624,1],[625,0],[626,0],[627,1],[628,0],[629,1],[630,0],[631,0],[632,0],[633,2],[634,1],[635,0],[636,1],[637,0],[638,5],[639,5],[640,5],[641,5],[642,5],[643,4],[644,4],[645,5],[646,4],[647,5],[648,4],[649,4],[650,2],[651,1],[652,0],[653,2],[654,1],[655,0],[656,2],[657,1],[658,0],[659,1],[660,0],[661,2],[662,1],[663,0],[664,2],[665,1],[666,0],[667,1],[668,0],[669,2],[670,1],[671,0],[672,1],[673,0],[674,1],[675,0],[676,0],[677,1],[678,0],[679,2],[680,1],[681,0],[682,1],[683,0],[684,1],[685,0],[686,1],[687,0],[688,1],[689,0],[690,1],[691,0],[692,1],[693,0],[694,1],[695,0],[696,1],[697,0],[698,1],[699,0],[700,0],[701,0],[702,0],[703,0],[704,2],[705,1],[706,0],[707,0],[708,1],[709,0],[710,1],[711,0],[712,1],[713,0],[714,1],[715,0],[716,4],[717,4],[718,4],[719,4],[720,4],[721,4],[722,2],[723,1],[724,0],[725,2],[726,1],[727,0],[728,2],[729,1],[730,0],[731,2],[732,1],[733,0],[734,1],[735,0],[736,2],[737,1],[738,0],[739,1],[740,0],[741,0],[742,1],[743,0],[744,1],[745,0],[746,4],[747,1],[748,0],[749,1],[750,0],[751,1],[752,0],[753,1],[754,0],[755,1],[756,0],[757,1],[758,0],[759,1],[760,0],[761,2],[762,1],[763,0],[764,0],[765,0],[766,0],[767,1],[768,0],[769,1],[770,0],[771,0],[772,1],[773,0],[774,0],[775,0],[776,0],[777,0],[778,0],[779,0],[780,0],[781,0],[782,2],[783,1],[784,0],[785,5],[786,5],[787,5],[788,5],[789,4],[790,4],[791,4],[792,4],[793,5],[794,5],[795,5],[796,5],[797,5],[798,5],[799,5],[800,4],[801,4],[802,4],[803,1],[804,5],[805,5],[806,5],[807,4],[808,4],[809,4],[810,4],[811,0],[812,0],[813,5],[814,4],[815,0],[816,0],[817,0],[818,0],[819,0],[820,0],[821,0],[822,0],[823,0],[824,1],[825,0],[826,0],[827,8],[828,5],[829,4],[830,4],[831,5],[832,5],[833,5],[834,5],[835,6],[836,0],[837,0],[838,0],[839,0],[840,0],[841,0],[842,0],[843,0],[844,0],[845,0],[846,6],[847,6],[848,6],[849,6],[850,6],[851,7],[852,7],[853,6],[854,6],[855,6],[856,6],[857,6],[858,6],[859,6],[860,6],[861,6],[862,6],[863,6],[864,0],[865,6],[866,6],[867,6],[868,6],[869,6],[870,6],[871,6],[872,6],[873,6],[874,7],[875,7],[876,1],[877,1],[878,1],[879,0],[880,0],[881,0],[882,1],[883,1],[884,1],[885,5],[886,0],[887,6],[888,6],[889,6],[890,6],[891,6],[892,6],[893,6],[894,6],[895,6],[896,6],[897,6],[898,6],[899,6],[900,7],[901,7],[902,7],[903,4],[904,6],[905,6],[906,6],[907,6],[908,6],[909,0],[910,0],[911,0],[912,0],[913,0],[914,1],[915,0],[916,0],[917,0],[918,1],[919,0],[920,1],[921,0],[922,1],[923,0],[924,2],[925,1],[926,0],[927,1],[928,0],[929,0],[930,0],[931,0],[932,0],[933,4],[934,4],[935,4],[936,4],[937,4],[938,0],[939,0],[940,0],[941,0],[942,0],[943,0],[944,8],[945,8],[946,8],[947,8],[948,8],[949,8],[950,8],[951,1],[952,0],[953,0],[954,0],[955,0],[956,0],[957,1],[958,1],[959,1],[960,1],[961,1],[962,1],[963,1],[964,0],[965,0],[966,0],[967,0],[968,0],[969,4],[970,4],[971,4],[972,0],[973,0],[974,0],[975,1]]

base_form_reference_gen_7 = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0],[42,0],[43,0],[44,0],[45,0],[46,0],[47,0],[48,0],[49,0],[50,0],[51,0],[52,0],[53,0],[54,0],[55,0],[56,0],[57,0],[58,0],[59,0],[60,0],[61,0],[62,0],[63,0],[64,0],[65,0],[66,0],[67,0],[68,0],[69,0],[70,0],[71,0],[72,0],[73,0],[74,0],[75,0],[76,0],[77,0],[78,0],[79,0],[80,0],[81,0],[82,0],[83,0],[84,0],[85,0],[86,0],[87,0],[88,0],[89,0],[90,0],[91,0],[92,0],[93,0],[94,0],[95,0],[96,0],[97,0],[98,0],[99,0],[100,0],[101,0],[102,0],[103,0],[104,0],[105,0],[106,0],[107,0],[108,0],[109,0],[110,0],[111,0],[112,0],[113,0],[114,0],[115,0],[116,0],[117,0],[118,0],[119,0],[120,0],[121,0],[122,0],[123,0],[124,0],[125,0],[126,0],[127,0],[128,0],[129,0],[130,0],[131,0],[132,0],[133,0],[134,0],[135,0],[136,0],[137,0],[138,0],[139,0],[140,0],[141,0],[142,0],[143,0],[144,0],[145,0],[146,0],[147,0],[148,0],[149,0],[150,0],[151,0],[152,0],[153,0],[154,0],[155,0],[156,0],[157,0],[158,0],[159,0],[160,0],[161,0],[162,0],[163,0],[164,0],[165,0],[166,0],[167,0],[168,0],[169,0],[170,0],[171,0],[172,0],[173,0],[174,0],[175,0],[176,0],[177,0],[178,0],[179,0],[180,0],[181,0],[182,0],[183,0],[184,0],[185,0],[186,0],[187,0],[188,0],[189,0],[190,0],[191,0],[192,0],[193,0],[194,0],[195,0],[196,0],[197,0],[198,0],[199,0],[200,0],[201,0],[202,0],[203,0],[204,0],[205,0],[206,0],[207,0],[208,0],[209,0],[210,0],[211,0],[212,0],[213,0],[214,0],[215,0],[216,0],[217,0],[218,0],[219,0],[220,0],[221,0],[222,0],[223,0],[224,0],[225,0],[226,0],[227,0],[228,0],[229,0],[230,0],[231,0],[232,0],[233,0],[234,0],[235,0],[236,0],[237,0],[238,0],[239,0],[240,0],[241,0],[242,0],[243,0],[244,0],[245,0],[246,0],[247,0],[248,0],[249,0],[250,0],[251,0],[252,0],[253,0],[254,0],[255,0],[256,0],[257,0],[258,0],[259,0],[260,0],[261,0],[262,0],[263,0],[264,0],[265,0],[266,0],[267,0],[268,0],[269,0],[270,0],[271,0],[272,0],[273,0],[274,0],[275,0],[276,0],[277,0],[278,0],[279,0],[280,0],[281,0],[282,0],[283,0],[284,0],[285,0],[286,0],[287,0],[288,0],[289,0],[290,0],[291,0],[292,0],[293,0],[294,0],[295,0],[296,0],[297,0],[298,0],[299,0],[300,0],[301,0],[302,0],[303,0],[304,0],[305,0],[306,0],[307,0],[308,0],[309,0],[310,0],[311,0],[312,0],[313,0],[314,0],[315,0],[316,0],[317,0],[318,0],[319,0],[320,0],[321,0],[322,0],[323,0],[324,0],[325,0],[326,0],[327,0],[328,0],[329,0],[330,0],[331,0],[332,0],[333,0],[334,0],[335,0],[336,0],[337,0],[338,0],[339,0],[340,0],[341,0],[342,0],[343,0],[344,0],[345,0],[346,0],[347,0],[348,0],[349,0],[350,0],[351,0],[352,0],[353,0],[354,0],[355,0],[356,0],[357,0],[358,0],[359,0],[360,0],[361,0],[362,0],[363,0],[364,0],[365,0],[366,0],[367,0],[368,0],[369,0],[370,0],[371,0],[372,0],[373,0],[374,0],[375,0],[376,0],[377,0],[378,0],[379,0],[380,0],[381,0],[382,0],[383,0],[384,0],[385,0],[386,0],[387,0],[388,0],[389,0],[390,0],[391,0],[392,0],[393,0],[394,0],[395,0],[396,0],[397,0],[398,0],[399,0],[400,0],[401,0],[402,0],[403,0],[404,0],[405,0],[406,0],[407,0],[408,0],[409,0],[410,0],[411,0],[412,0],[413,0],[414,0],[415,0],[416,0],[417,0],[418,0],[419,0],[420,0],[421,0],[422,0],[423,0],[424,0],[425,0],[426,0],[427,0],[428,0],[429,0],[430,0],[431,0],[432,0],[433,0],[434,0],[435,0],[436,0],[437,0],[438,0],[439,0],[440,0],[441,0],[442,0],[443,0],[444,0],[445,0],[446,0],[447,0],[448,0],[449,0],[450,0],[451,0],[452,0],[453,0],[454,0],[455,0],[456,0],[457,0],[458,0],[459,0],[460,0],[461,0],[462,0],[463,0],[464,0],[465,0],[466,0],[467,0],[468,0],[469,0],[470,0],[471,0],[472,0],[473,0],[474,0],[475,0],[476,0],[477,0],[478,0],[479,0],[480,0],[481,0],[482,0],[483,0],[484,0],[485,0],[486,0],[487,0],[488,0],[489,0],[490,0],[491,0],[492,0],[493,0],[494,0],[495,0],[496,0],[497,0],[498,0],[499,0],[500,0],[501,0],[502,0],[503,0],[504,0],[505,0],[506,0],[507,0],[508,0],[509,0],[510,0],[511,0],[512,0],[513,0],[514,0],[515,0],[516,0],[517,0],[518,0],[519,0],[520,0],[521,0],[522,0],[523,0],[524,0],[525,0],[526,0],[527,0],[528,0],[529,0],[530,0],[531,0],[532,0],[533,0],[534,0],[535,0],[536,0],[537,0],[538,0],[539,0],[540,0],[541,0],[542,0],[543,0],[544,0],[545,0],[546,0],[547,0],[548,0],[549,0],[550,0],[551,0],[552,0],[553,0],[554,0],[555,0],[556,0],[557,0],[558,0],[559,0],[560,0],[561,0],[562,0],[563,0],[564,0],[565,0],[566,0],[567,0],[568,0],[569,0],[570,0],[571,0],[572,0],[573,0],[574,0],[575,0],[576,0],[577,0],[578,0],[579,0],[580,0],[581,0],[582,0],[583,0],[584,0],[585,0],[586,0],[587,0],[588,0],[589,0],[590,0],[591,0],[592,0],[593,0],[594,0],[595,0],[596,0],[597,0],[598,0],[599,0],[600,0],[601,0],[602,0],[603,0],[604,0],[605,0],[606,0],[607,0],[608,0],[609,0],[610,0],[611,0],[612,0],[613,0],[614,0],[615,0],[616,0],[617,0],[618,0],[619,0],[620,0],[621,0],[622,0],[623,0],[624,0],[625,0],[626,0],[627,0],[628,0],[629,0],[630,0],[631,0],[632,0],[633,0],[634,0],[635,0],[636,0],[637,0],[638,0],[639,0],[640,0],[641,0],[642,0],[643,0],[644,0],[645,0],[646,0],[647,0],[648,0],[649,0],[650,0],[651,0],[652,0],[653,0],[654,0],[655,0],[656,0],[657,0],[658,0],[659,0],[660,0],[661,0],[662,0],[663,0],[664,0],[665,0],[666,0],[667,0],[668,0],[669,0],[670,0],[671,0],[672,0],[673,0],[674,0],[675,0],[676,0],[677,0],[678,0],[679,0],[680,0],[681,0],[682,0],[683,0],[684,0],[685,0],[686,0],[687,0],[688,0],[689,0],[690,0],[691,0],[692,0],[693,0],[694,0],[695,0],[696,0],[697,0],[698,0],[699,0],[700,0],[701,0],[702,0],[703,0],[704,0],[705,0],[706,0],[707,0],[708,0],[709,0],[710,0],[711,0],[712,0],[713,0],[714,0],[715,0],[716,0],[717,0],[718,0],[719,0],[720,0],[721,0],[722,0],[723,0],[724,0],[725,0],[726,0],[727,0],[728,0],[729,0],[730,0],[731,0],[732,0],[733,0],[734,0],[735,0],[736,0],[737,0],[738,0],[739,0],[740,0],[741,0],[742,0],[743,0],[744,0],[745,0],[746,0],[747,0],[748,0],[749,0],[750,0],[751,0],[752,0],[753,0],[754,0],[755,0],[756,0],[757,0],[758,0],[759,0],[760,0],[761,0],[762,0],[763,0],[764,0],[765,0],[766,0],[767,0],[768,0],[769,0],[770,0],[771,0],[772,0],[773,0],[774,0],[775,0],[776,0],[777,0],[778,0],[779,0],[780,0],[781,0],[782,0],[783,0],[784,0],[785,0],[786,0],[787,0],[788,0],[789,0],[790,0],[791,0],[792,0],[793,0],[794,0],[795,0],[796,0],[797,0],[798,0],[799,0],[800,0],[801,0],[802,0],[803,0],[804,0],[805,0],[806,0],[807,0],[808,0],[809,0],[810,0],[811,0],[812,0],[813,0],[814,0],[815,0],[816,0],[817,0],[818,0],[819,0],[820,0],[821,0],[822,0],[823,0],[824,0],[825,0],[826,0],[827,555],[828,0],[829,0],[830,0],[831,0],[832,0],[833,0],[834,0],[835,94],[836,0],[837,0],[838,0],[839,0],[840,0],[841,0],[842,0],[843,0],[844,0],[845,0],[846,282],[847,181],[848,3],[849,6],[850,6],[851,150],[852,150],[853,257],[854,308],[855,229],[856,306],[857,354],[858,248],[859,212],[860,127],[861,142],[862,448],[863,460],[864,0],[865,9],[866,115],[867,130],[868,359],[869,65],[870,214],[871,303],[872,310],[873,445],[874,381],[875,380],[876,0],[877,0],[878,0],[879,0],[880,0],[881,0],[882,0],[883,0],[884,0],[885,0],[886,0],[887,260],[888,254],[889,302],[890,334],[891,475],[892,531],[893,319],[894,80],[895,208],[896,18],[897,362],[898,719],[899,376],[900,0],[901,0],[902,0],[903,0],[904,323],[905,428],[906,373],[907,15],[908,746],[909,0],[910,0],[911,0],[912,0],[913,0],[914,0],[915,0],[916,0],[917,0],[918,0],[919,0],[920,0],[921,0],[922,0],[923,0],[924,0],[925,0],[926,0],[927,0],[928,0],[929,0],[930,0],[931,0],[932,0],[933,0],[934,0],[935,0],[936,0],[937,0],[938,0],[939,0],[940,0],[941,0],[942,0],[943,0],[944,943],[945,943],[946,943],[947,943],[948,943],[949,943],[950,943],[951,0],[952,0],[953,0],[954,0],[955,0],[956,0],[957,0],[958,0],[959,0],[960,0],[961,0],[962,0],[963,0],[964,0],[965,0],[966,0],[967,0],[968,0],[969,0],[970,0],[971,0],[972,0],[973,0],[974,0],[975,0]]





def get_data():
	with open("text.txt") as f:
		line = f.readlines()
		f.close()
	
	#line is a list with the entire text in its first entry, this turns the string into a by-character array
	data = []
	
	for char in line[0]:
		data.append(char)
	
	return(data)

def get_hex_pair(position, data):
	curr_character = data[position]
	one_ago_character = data[position - 1]
	two_ago_character = data[position - 2]
	
	return(curr_character, one_ago_character, two_ago_character)
	
def manipulate(gen_number):

	
	if(gen_number == 7):
		data_skip = data_skip_7
		pokemon = pokemon_gen_7
		in_first_block = True
	elif(gen_number == 4):
		data_skip = data_skip_4
		pokemon = pokemon_gen_4
	
	max_index = len(pokemon) - 1
	
	data = get_data()
	print(len(data))
	stats_counted = 0
	
	stat_arr = [0, 0, 0, 0, 0, 0]
	
	hex_arr = ['FF','FF','FF','FF','FF','FF']
	
	stat_sum = 0
	
	#Start with the first triplet - Bulba's HP and the following space
	position = 2
	
	dex_number = 1
	
	output_stats = [["HP","ATK","DEF","SPD","SpA","SpD"]]
	mega_list = []
	
	#read the file character by character
	while True:
		#if the character is a space
		
		curr_character, one_ago_character, two_ago_character = get_hex_pair(position, data)
		
		#grabs a stat
		if(curr_character == " "):
			#looks like  "DF ", gives "DF", then convert the hex to an integer (need to remove the string property anyway) and write the stat to the stat array
			stat_arr[stats_counted] = int(two_ago_character + one_ago_character, 16)

			
			stat_sum += stat_arr[stats_counted]
			
			#counts how many stats we've counted
			stats_counted += 1
		
		#if we've gotten all six stats
		if(stats_counted == 6):
			#reset the counter
			stats_counted = 0
						
			#if the Pokemon is a Mega, copy the HP from the base form:
			if(pokemon[dex_number][1] == 6 or pokemon[dex_number][1] == 8):
				#calls the updated HP from the base form (HP is the first stat)
				base_number = base_form_reference_gen_7[dex_number][1]
				stat_arr[0] = output_stats[base_number][1][0]

			#scale the stats
			for counter, stat in enumerate(stat_arr):
				
				#evolves one more time
				if(pokemon[dex_number][1] == 1):
					stat_arr[counter] = round((stat*400)/stat_sum)
				#evolves two more times
				elif(pokemon[dex_number][1] == 2):
					stat_arr[counter] = round((stat*300)/stat_sum)
				#shedinja, scale everything to 400 but don't scale HP
				elif(dex_number == 292):
					if(counter != 0):
						stat_arr[counter] = round((stat*400)/(stat_sum))
				#fully evolved or Legendary with <= 600 BST (scale to 600)
				elif(pokemon[dex_number][1] == 0 or pokemon[dex_number][1] == 5):
					stat_arr[counter] = round((stat*600)/stat_sum)
				#Mega Evolution of a Pokemon with <= 600 BST (Mega has <= 700 BST) (scale to 700)
				elif(pokemon[dex_number][1] == 6):
					#don't change HP
					if(counter != 0):
						stat_arr[counter] = round((stat*(700 - stat_arr[0]))/(stat_sum - stat_arr[0]))
				elif(pokemon[dex_number][1] == 8):
					#don't change HP
					if(counter != 0):
						print(dex_number)
						stat_arr[counter] = round((stat*(600 - stat_arr[0]))/(stat_sum - stat_arr[0]))
				#Legendary with BST > 600 (no scale)
				elif(pokemon[dex_number][1] == 4):
					stat_arr[counter] = stat
				#egg (no scale)
				elif(pokemon[dex_number][1] == 3):
					stat_arr[counter] = stat
			

			#scale Shedinja using Ninjask's base HP, then reset its HP to 1
			if(dex_number == 292):
				stat_arr[0] = 1
			
			#if stat is over 255, redistribute the excess
			while True:
				
				overage_count = 0
				overage = 0
				#checks if there is anything over 255
				for counter, stat in enumerate(stat_arr):
					if(stat > 255):
						overage_count += 1
						overage += stat - 255
						stat_arr[counter] = 255
				#if nothing is over 255, proceed
				if(overage == 0):
					break
				#otherwise redistribute, then loop around to make sure we didn't break anything else
				else:
					#if the Pokemon is a Mega, don't change HP
					if(pokemon[dex_number][1] == 6):
						redistribute = round(overage/(5 - overage_count))
						for counter, stat in enumerate(stat_arr):
							if(stat != 255 and counter != 0):
								stat_arr[counter] = stat + redistribute
					else:
						redistribute = round(overage/(6 - overage_count))
						for counter, stat in enumerate(stat_arr):
							if(stat != 255):
								stat_arr[counter] = stat + redistribute
								

			#checks if the rounding error is greater 5, for Megas, who have this problem

			
			if(pokemon[dex_number][1] == 6):
				while True:
					BST = 0
					for counter, stat in enumerate(stat_arr):
						BST += stat
					rounding_error = BST - 700
					
					#if I can subtract 1 from each non-HP stat (because this should only happen to Pokemon that had weird scaling, the Megas), and still be above the intended BST, do so
					if(rounding_error >= 5):
						for counter, stat in enumerate(stat_arr):
							if(counter != 0):
								stat_arr[counter] = stat - 1
					#if that much below, add 5
					elif(rounding_error <= -5):
						for counter, stat in enumerate(stat_arr):
							if(counter != 0):
								stat_arr[counter] = stat + 1
					#otherwise, we're good, so end this loop
					else:
						break
				#write the non-Mega/Mega pair to the list
				mega_list.append([base_number, dex_number])
			
			

			temp = []
			for stat in stat_arr:
				temp.append(stat)
			
			
			
			#sticks the new stats in this array
			output_stats.append([dex_number, temp])
			#overwrite the source string with the new values
			
			for counter, x in enumerate(stat_arr):
				
				#if the hex number x has a trailing 0 (it looks like h0 for a digit h), hex(x)[2:4] will truncate the 0, leading to an error. In this case, write h0 to the array
				
				#catch x < 16
				if(x < 16):
					temp_hex = '0' + str(hex(x)[2:4])
				#catch if x is of the form h0
				elif(x%16 == 0):
					temp_hex = str(hex(x)[2:4])
				#otherwise, we're good
				else:
					temp_hex = hex(x)[2:4]
				
				hex_arr[counter] = temp_hex
				
			#each position 'block' is three characters. We are in the third character of the sixth set, need to start from 1rst of 1rst. A:123 B:456 C:789 D:10,11,12 E:13,14,15 F:16,17,18. need position - 17
			
			temp_pos = position - 17
			stat_number = 0
			
			while True:
				#write the first hex digit to the first of the pair
				data[temp_pos] = hex_arr[stat_number][0]
				#write the second to the second
				data[temp_pos + 1] = hex_arr[stat_number][1]
				
				#if we've written all six stats, break
				if(stat_number >= 5):
					break
				#otherwise go to next stat
				else:
					stat_number += 1
					temp_pos += 3
			#change Slakoth's and Slaking's Abilities to Comatose. We are in position 1 + 3*5 = 16 = temp_pos need to write to that plus 57 for Ability 1, three more for Ability 2, three more for Hidden Ability
			if(dex_number == 287 or dex_number == 289):
				#Ability 1
				data[temp_pos + 57] = 'D'
				data[temp_pos + 58] = '5'
				#Ability 1
				data[temp_pos + 60] = 'D'
				data[temp_pos + 61] = '5'
				#Ability 1
				data[temp_pos + 63] = 'D'
				data[temp_pos + 64] = '5'
				
			#change Regigigas' Abilities to Sheer Force
			if(dex_number == 486):
				#Ability 1
				data[temp_pos + 57] = '7'
				data[temp_pos + 58] = 'D'
				#Ability 1
				data[temp_pos + 60] = '7'
				data[temp_pos + 61] = 'D'
				#Ability 1
				data[temp_pos + 63] = '7'
				data[temp_pos + 64] = 'D'
			
			if(dex_number == max_index):
				
				#gen vii has a second, repeat block
				if(gen_number == 7):
					if(in_first_block):
						in_first_block = False
						position = 245954 - 252 + 15
						#will get incremented at the end of the loop
						dex_number = 0
						data_skip = 252 - 15
						
						#print list of modified stats
						for elm in output_stats:
							print(elm)	
						
						#print mega and base list
						if(gen_number >= 6):
							print('\n')
							for elm in mega_list:
								print(output_stats[elm[0]])
								print("m", output_stats[elm[1]])
					else:		
						#data is an array, make it back into a string
						out_string = ''
						for char in data:
							out_string += char
					
						with open('text_out.txt', 'w') as d:
							d.write(out_string)
						break
				else:		
					#data is an array, make it back into a string
					out_string = ''
					for char in data:
						out_string += char
				
					with open('text_out.txt', 'w') as d:
						d.write(out_string)
					break
				
			#zero out the stat array and sum
			for stat in stat_arr:
				stat_arr[counter] = 0
			stat_sum = 0
			stats_counted = 0
			
			#jump to the start of the next Pokemon 
			position += data_skip
			
			
			#next index number
			dex_number += 1
		#otherwise, get the next stat
		else:
			position += 3

			
def report_original_stats(gen_number):

	if(gen_number == 7):
		data_skip = data_skip_7
		pokemon = pokemon_gen_7
	elif(gen_number == 4):
		data_skip = data_skip_4
		pokemon = pokemon_gen_4
	
	max_index = len(pokemon) - 1
	
	data = get_data()
	stats_counted = 0
	
	stat_arr = [0, 0, 0, 0, 0, 0]
	
	#Start with the first triplet - Bulba's HP and the following space
	position = 2
	
	dex_number = 1
	
	output_stats = [["HP","ATK","DEF","SPD","SpA","SpD"]]
	
	#read the file character by character
	while True:
		#if the character is a space
		
		curr_character, one_ago_character, two_ago_character = get_hex_pair(position, data)
		
		#grabs a stat
		if(curr_character == " "):
			#looks like  "DF ", gives "DF", then convert the hex to an integer (need to remove the string property anyway) and write the stat to the stat array
			stat_arr[stats_counted] = int(two_ago_character + one_ago_character, 16)
			
			#counts how many stats we've counted
			stats_counted += 1
		
		if(stats_counted == 6):
			print(dex_number, stat_arr)
		
			if(dex_number == max_index):
				break
			#zero out the stat array and sum
			for counter, stat in enumerate(stat_arr):
				stat_arr[counter] = 0
			stat_sum = 0
			stats_counted = 0
			
			#jump to the start of the next Pokemon 
			position += data_skip
			
			#next index number
			dex_number += 1
		else:
			position += 3

#report_original_stats(7)
manipulate(7)



