---
layout: single
title: CSHI vs BIL
excerpt: CSHI의 최근 2년 1개월 CAGR은 5.5%로 BIL의 4.8%와 비슷했습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: BIL, CSHI, CSHI BIL 비교
---

## 비교 상품 소개


CSHI 상품과 BIL 상품의 성과를 수익률과 위험도로 비교합니다.





{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 2년 1개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.
하단의 보조 그래프는 BIL 대비 CSHI의 비를 나타냅니다.
CSHI의 수익률이 BIL보다 지속적으로 우세하면 상승하고, 반대의 경우에는 하락합니다.

![CSHI](/vs/images/cshi-vs-bil_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| CSHI | <span style="color: tomato">5.5<small>%</small></span> | 1.0<small>%</small> | 5.25 | -0.4<small>%</small> | -0.0<small>%</small> |
| BIL | <span style="color: tomato">4.8<small>%</small></span> | 0.3<small>%</small> | 17.40 | -0.0<small>%</small> | -0.0<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** CSHI의 CAGR은 5.5%로 BIL의 4.8%와 비슷했습니다. (비슷한 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** CSHI의 표준편차는 1.0%로 BIL의 0.3%와 비슷했습니다. (비슷한 위험도)

**위험도 지표 (MDD):** CSHI의 0.4%의 MDD는 BIL의 0.0%와 비슷했습니다. (비슷한 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 BIL의 투자 비중[^fn_vs_weight]을 조절하여 CSHI의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 0.3% / 1.0% = 379% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 0.0% / 0.4% = 1471% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
BIL<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, BIL<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![CSHI](/vs/images/cshi-vs-bil.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| CSHI | <span style="color: tomato">5.5<small>%</small></span> | 1.0<small>%</small> | 5.25 | -0.4<small>%</small> | -0.0<small>%</small> |
| BIL | <span style="color: tomato">4.8<small>%</small></span> | 0.3<small>%</small> | 17.40 | -0.0<small>%</small> | -0.0<small>%</small> |
| BIL<sub>STD</sub> <small>(379%)</small> | <span style="color: tomato">19.5<small>%</small></span> | 1.0<small>%</small> | 18.59 | -0.1<small>%</small> | -0.0<small>%</small> |
| BIL<sub>MDD</sub> <small>(1471%)</small> | <span style="color: tomato">99.1<small>%</small></span> | 4.1<small>%</small> | 24.40 | -0.4<small>%</small> | -0.0<small>%</small> |



각각의 경우를 CSHI의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 379% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 19.5%로 CSHI의 5.5%보다 14.0% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 1471% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 99.1%로 CSHI의 5.5%보다 93.6% 높았습니다. (높은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 2년 1개월간 거치식으로 투자했다고 가정합니다.

BIL의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 59.3%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 CSHI의 5.5%보다 53.8% 높았습니다.

### CSHI	&lt; BIL
{: .text-center}


## 관련 정보

- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}