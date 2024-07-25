---
layout: single
title: JEPY vs SPY
excerpt: JEPY의 최근 9개월 CAGR은 15.1%로 SPY의 27.5%보다 -12.4% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: SPY, JEPY, JEPY SPY 비교
---

## 비교 상품 소개


S&P 500 지수에 대해 데일리 커버드 콜 전략을 쓰는 JEPY와 S&P 500 지수를 추종하는 SPY의 성과를 비교해 봅니다.



{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 9개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.
하단의 보조 그래프는 SPY 대비 JEPY의 비를 나타냅니다.
JEPY의 수익률이 SPY보다 지속적으로 우세하면 상승하고, 반대의 경우에는 하락합니다.

![JEPY](/vs/images/jepy-vs-spy_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| JEPY | <span style="color: tomato">15.1<small>%</small></span> | 7.7<small>%</small> | 1.97 | -4.3<small>%</small> | -0.8<small>%</small> |
| SPY | <span style="color: tomato">27.5<small>%</small></span> | 11.5<small>%</small> | 2.38 | -7.2<small>%</small> | -1.2<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** JEPY의 CAGR은 15.1%로 SPY의 27.5%보다 -12.4% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** JEPY의 표준편차는 7.7%로 SPY의 11.5%보다 -3.9% 낮았습니다. (낮은 위험도)

**위험도 지표 (MDD):** JEPY의 4.3%의 MDD는 SPY의 7.2%보다 -2.9% 낮았습니다. (낮은 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 SPY의 투자 비중[^fn_vs_weight]을 조절하여 JEPY의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 11.5% / 7.7% = 67% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 7.2% / 4.3% = 59% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
SPY<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, SPY<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![JEPY](/vs/images/jepy-vs-spy.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| JEPY | <span style="color: tomato">15.1<small>%</small></span> | 7.7<small>%</small> | 1.97 | -4.3<small>%</small> | -0.8<small>%</small> |
| SPY | <span style="color: tomato">27.5<small>%</small></span> | 11.5<small>%</small> | 2.38 | -7.2<small>%</small> | -1.2<small>%</small> |
| SPY<sub>STD</sub> <small>(67%)</small> | <span style="color: tomato">17.7<small>%</small></span> | 7.7<small>%</small> | 2.31 | -4.9<small>%</small> | -0.8<small>%</small> |
| SPY<sub>MDD</sub> <small>(59%)</small> | <span style="color: tomato">15.7<small>%</small></span> | 6.8<small>%</small> | 2.29 | -4.3<small>%</small> | -0.7<small>%</small> |



각각의 경우를 JEPY의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 67% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 17.7%로 JEPY의 15.1%보다 2.6% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 59% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 15.7%로 JEPY의 15.1%와 비슷했습니다. (비슷한 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 9개월간 거치식으로 투자했다고 가정합니다.

SPY의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 16.7%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 JEPY의 15.1%보다 1.6% 높았습니다.

### JEPY	&lt; SPY
{: .text-center}


## 관련 정보

- [한국인도 ROC(Return of Capital) 비과세 적용을 받을 수 있습니다. (배당소득재분류에 따른 현지 배당세 환급 및 국내 배당세 징수)](https://kongdori.tistory.com/299)
- [초고배당 커버드콜 ETF는 기초 자산보다 현금 흐름 창출에 유리할까? (TSLY, NVDY, JEPY, QQQY 등 22종의 커버드콜 ETF 분석)](https://kongdori.tistory.com/286)
- [ISPY - ProShares의 초단기 콜옵션 전략 기반 인컴 ETF (넌 누굴 닮았니?)](https://kongdori.tistory.com/267)
- [BALI - 블랙록의 커버드콜 기반 인컴 ETF (발리섬에서 은퇴 생활을 즐길 수 있을까? JEPQ의 S&P500 버전)](https://kongdori.tistory.com/261)
- [JEPI - CALL = ? (JEPI/JEPQ의 내부는 어떤 액티브 ETF일까?)](https://kongdori.tistory.com/256)
- [데일리 커버드콜은 효과적일까? (Defiance의 JEPY, QQQY, IWMY - 분배율 높은 인컴 ETF)](https://kongdori.tistory.com/235)
- [원금 찾는데 세금을 내라고? (해외 상장 고배당 인컴 ETF)](https://kongdori.tistory.com/206)
- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}