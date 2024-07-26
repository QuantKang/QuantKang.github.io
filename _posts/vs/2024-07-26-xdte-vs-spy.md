---
layout: single
title: XDTE vs SPY
excerpt: XDTE의 최근 4개월 CAGR은 14.9%로 SPY의 17.5%보다 -2.6% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: SPY, XDTE, XDTE SPY 비교
---

## 비교 상품 소개


XDTE 상품과 SPY 상품의 성과를 수익률과 위험도로 비교합니다.





{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 4개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.
하단의 보조 그래프는 SPY 대비 XDTE의 비를 나타냅니다.
XDTE의 수익률이 SPY보다 지속적으로 우세하면 상승하고, 반대의 경우에는 하락합니다.

![XDTE](/vs/images/xdte-vs-spy_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| XDTE | <span style="color: tomato">14.9<small>%</small></span> | 10.0<small>%</small> | 1.49 | -5.0<small>%</small> | -1.0<small>%</small> |
| SPY | <span style="color: tomato">17.5<small>%</small></span> | 10.9<small>%</small> | 1.60 | -5.4<small>%</small> | -1.1<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** XDTE의 CAGR은 14.9%로 SPY의 17.5%보다 -2.6% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** XDTE의 표준편차는 10.0%로 SPY의 10.9%와 비슷했습니다. (비슷한 위험도)

**위험도 지표 (MDD):** XDTE의 5.0%의 MDD는 SPY의 5.4%와 비슷했습니다. (비슷한 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 SPY의 투자 비중[^fn_vs_weight]을 조절하여 XDTE의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 10.9% / 10.0% = 91% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 5.4% / 5.0% = 94% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
SPY<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, SPY<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![XDTE](/vs/images/xdte-vs-spy.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| XDTE | <span style="color: tomato">14.9<small>%</small></span> | 10.0<small>%</small> | 1.49 | -5.0<small>%</small> | -1.0<small>%</small> |
| SPY | <span style="color: tomato">17.5<small>%</small></span> | 10.9<small>%</small> | 1.60 | -5.4<small>%</small> | -1.1<small>%</small> |
| SPY<sub>STD</sub> <small>(91%)</small> | <span style="color: tomato">15.9<small>%</small></span> | 10.0<small>%</small> | 1.60 | -4.9<small>%</small> | -1.0<small>%</small> |
| SPY<sub>MDD</sub> <small>(94%)</small> | <span style="color: tomato">16.5<small>%</small></span> | 10.3<small>%</small> | 1.60 | -5.1<small>%</small> | -1.1<small>%</small> |



각각의 경우를 XDTE의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 91% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 15.9%로 XDTE의 14.9%보다 1.0% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 94% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 16.5%로 XDTE의 14.9%보다 1.6% 높았습니다. (높은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 4개월간 거치식으로 투자했다고 가정합니다.

SPY의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 16.2%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 XDTE의 14.9%보다 1.3% 높았습니다.

### XDTE	&lt; SPY
{: .text-center}


## 관련 정보

- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}