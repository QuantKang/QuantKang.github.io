---
layout: single
title: ARKK vs QQQ
excerpt: ARKK의 최근 9년 8개월 CAGR은 9.9%로 QQQ의 18.8%보다 -8.9% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: QQQ, ARKK, ARKK QQQ 비교
---

## 비교 상품 소개


QQQ 상품과 ARKK 상품의 성과를 수익률과 위험도로 비교합니다.





{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 9년 8개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.

![ARKK](/vs/images/arkk-vs-qqq_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| ARKK | <span style="color: tomato">9.9<small>%</small></span> | 37.4<small>%</small> | 0.27 | -80.9<small>%</small> | -24.6<small>%</small> |
| QQQ | <span style="color: tomato">18.8<small>%</small></span> | 21.7<small>%</small> | 0.87 | -35.1<small>%</small> | -6.3<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** ARKK의 CAGR은 9.9%로 QQQ의 18.8%보다 -8.9% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** ARKK의 표준편차는 37.4%로 QQQ의 21.7%보다 15.8% 높았습니다. (높은 위험도)

**위험도 지표 (MDD):** ARKK의 80.9%의 MDD는 QQQ의 35.1%보다 45.8% 높았습니다. (높은 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 QQQ의 투자 비중[^fn_vs_weight]을 조절하여 ARKK의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 21.7% / 37.4% = 173% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 35.1% / 80.9% = 230% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
QQQ<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, QQQ<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![ARKK](/vs/images/arkk-vs-qqq.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| ARKK | <span style="color: tomato">9.9<small>%</small></span> | 37.4<small>%</small> | 0.27 | -80.9<small>%</small> | -24.6<small>%</small> |
| QQQ | <span style="color: tomato">18.8<small>%</small></span> | 21.7<small>%</small> | 0.87 | -35.1<small>%</small> | -6.3<small>%</small> |
| QQQ<sub>STD</sub> <small>(173%)</small> | <span style="color: tomato">30.6<small>%</small></span> | 37.4<small>%</small> | 0.82 | -55.7<small>%</small> | -11.3<small>%</small> |
| QQQ<sub>MDD</sub> <small>(230%)</small> | <span style="color: tomato">38.3<small>%</small></span> | 49.9<small>%</small> | 0.77 | -68.6<small>%</small> | -15.5<small>%</small> |



각각의 경우를 ARKK의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 173% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 30.6%로 ARKK의 9.9%보다 20.7% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 230% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 38.3%로 ARKK의 9.9%보다 28.4% 높았습니다. (높은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 9년 8개월간 거치식으로 투자했다고 가정합니다.

QQQ의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 34.5%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 ARKK의 9.9%보다 24.6% 높았습니다.

### ARKK	&lt; QQQ
{: .text-center}


## 관련 정보

- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}