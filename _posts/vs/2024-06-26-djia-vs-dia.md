---
layout: single
title: DJIA vs DIA
excerpt: DJIA의 최근 2년 3개월 CAGR은 4.4%로 DIA의 9.4%보다 -5.0% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: DIA, DJIA, DJIA DIA 비교
---

## 비교 상품 소개


전통이 깊은 다우 존스 산업평균지수에 대해 커버드 콜 전략을 쓰는 DIJA를 해당 지수를 추종하는 DIA와 비교해 봅니다.



## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 2년 3개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.

![DJIA](/vs/images/djia-vs-dia_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| DJIA | <span style="color: tomato">4.4<small>%</small></span> | 11.1<small>%</small> | 0.40 | -16.9<small>%</small> | -5.0<small>%</small> |
| DIA | <span style="color: tomato">9.4<small>%</small></span> | 15.0<small>%</small> | 0.62 | -17.8<small>%</small> | -4.1<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** DJIA의 CAGR은 4.4%로 DIA의 9.4%보다 -5.0% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** DJIA의 표준편차는 11.1%로 DIA의 15.0%보다 -4.0% 낮았습니다. (낮은 위험도)

**위험도 지표 (MDD):** DJIA의 16.9%의 MDD는 DIA의 17.8%와 비슷했습니다. (비슷한 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 DIA의 투자 비중[^fn_vs_weight]을 조절하여 DJIA의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 15.0% / 11.1% = 74% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 17.8% / 16.9% = 95% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
DIA<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, DIA<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![DJIA](/vs/images/djia-vs-dia.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| DJIA | <span style="color: tomato">4.4<small>%</small></span> | 11.1<small>%</small> | 0.40 | -16.9<small>%</small> | -5.0<small>%</small> |
| DIA | <span style="color: tomato">9.4<small>%</small></span> | 15.0<small>%</small> | 0.62 | -17.8<small>%</small> | -4.1<small>%</small> |
| DIA<sub>STD</sub> <small>(74%)</small> | <span style="color: tomato">7.0<small>%</small></span> | 11.1<small>%</small> | 0.64 | -13.2<small>%</small> | -2.9<small>%</small> |
| DIA<sub>MDD</sub> <small>(95%)</small> | <span style="color: tomato">8.9<small>%</small></span> | 14.3<small>%</small> | 0.62 | -16.9<small>%</small> | -3.9<small>%</small> |



각각의 경우를 DJIA의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 74% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 7.0%로 DJIA의 4.4%보다 2.7% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 95% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 8.9%로 DJIA의 4.4%보다 4.6% 높았습니다. (높은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 2년 3개월간 거치식으로 투자했다고 가정합니다.

DIA의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 8.0%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 DJIA의 4.4%보다 3.6% 높았습니다.

### DJIA	&lt; DIA
{: .text-center}


## 관련 정보

- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}