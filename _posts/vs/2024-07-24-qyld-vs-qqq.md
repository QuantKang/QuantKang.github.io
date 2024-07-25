---
layout: single
title: QYLD vs QQQ
excerpt: QYLD의 최근 10년 7개월 CAGR은 7.1%로 QQQ의 18.4%보다 -11.2% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: QQQ, QYLD, QYLD QQQ 비교
---

## 비교 상품 소개


나스닥 100 지수에 대해 커버드 콜 전략을 쓰는 QYLD와 나스닥 100 지수를 추종하는 QQQ의 성과를 비교해 봅니다.



{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 10년 7개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.
하단의 보조 그래프는 QQQ 대비 QYLD의 비를 나타냅니다.
QYLD의 수익률이 QQQ보다 지속적으로 우세하면 상승하고, 반대의 경우에는 하락합니다.

![QYLD](/vs/images/qyld-vs-qqq_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| QYLD | <span style="color: tomato">7.1<small>%</small></span> | 14.6<small>%</small> | 0.49 | -24.8<small>%</small> | -4.1<small>%</small> |
| QQQ | <span style="color: tomato">18.4<small>%</small></span> | 21.1<small>%</small> | 0.87 | -35.1<small>%</small> | -5.9<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** QYLD의 CAGR은 7.1%로 QQQ의 18.4%보다 -11.2% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** QYLD의 표준편차는 14.6%로 QQQ의 21.1%보다 -6.5% 낮았습니다. (낮은 위험도)

**위험도 지표 (MDD):** QYLD의 24.8%의 MDD는 QQQ의 35.1%보다 -10.4% 낮았습니다. (낮은 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 QQQ의 투자 비중[^fn_vs_weight]을 조절하여 QYLD의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 21.1% / 14.6% = 69% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 35.1% / 24.8% = 70% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
QQQ<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, QQQ<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![QYLD](/vs/images/qyld-vs-qqq.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| QYLD | <span style="color: tomato">7.1<small>%</small></span> | 14.6<small>%</small> | 0.49 | -24.8<small>%</small> | -4.1<small>%</small> |
| QQQ | <span style="color: tomato">18.4<small>%</small></span> | 21.1<small>%</small> | 0.87 | -35.1<small>%</small> | -5.9<small>%</small> |
| QQQ<sub>STD</sub> <small>(69%)</small> | <span style="color: tomato">12.9<small>%</small></span> | 14.6<small>%</small> | 0.88 | -25.1<small>%</small> | -4.0<small>%</small> |
| QQQ<sub>MDD</sub> <small>(70%)</small> | <span style="color: tomato">13.1<small>%</small></span> | 14.9<small>%</small> | 0.88 | -25.6<small>%</small> | -4.1<small>%</small> |



각각의 경우를 QYLD의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 69% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 12.9%로 QYLD의 7.1%보다 5.8% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 70% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 13.1%로 QYLD의 7.1%보다 6.0% 높았습니다. (높은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 10년 7개월간 거치식으로 투자했다고 가정합니다.

QQQ의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 13.0%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 QYLD의 7.1%보다 5.9% 높았습니다.

### QYLD	&lt; QQQ
{: .text-center}


## 관련 정보

- [JEPI - CALL = ? (JEPI/JEPQ의 내부는 어떤 액티브 ETF일까?)](https://kongdori.tistory.com/256)
- [커버드콜 ETF는 왜 장기 투자에 적합하지 않은가? (효율적 투자선과 50% 오렌지 주스)](https://kongdori.tistory.com/244)
- [커버드콜 ETF는 왜 하락장과 횡보장에서 좋은 성과를 거두지 못하는 것일까? (QYLD의 사례)](https://kongdori.tistory.com/240)
- [커버드콜은 정말 하락장과 횡보장에 유리할까?](https://kongdori.tistory.com/238)
- [커버드 콜 전략은 유용한가? (커버드 콜 전략을 쓰는 주요 ETF의 지금까지 수익률과 분석)](https://kongdori.tistory.com/155)
- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}