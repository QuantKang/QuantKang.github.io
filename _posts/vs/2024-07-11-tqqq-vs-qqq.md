---
layout: single
title: TQQQ vs QQQ
excerpt: TQQQ의 최근 14년 4개월 CAGR은 43.9%로 QQQ의 19.4%보다 24.5% 높았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: QQQ, TQQQ, TQQQ QQQ 비교
---

## 비교 상품 소개


TQQQ 상품과 QQQ 상품의 성과를 수익률과 위험도로 비교합니다.





{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 14년 4개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.

![TQQQ](/vs/images/tqqq-vs-qqq_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| TQQQ | <span style="color: tomato">43.9<small>%</small></span> | 60.2<small>%</small> | 0.73 | -81.7<small>%</small> | -19.0<small>%</small> |
| QQQ | <span style="color: tomato">19.4<small>%</small></span> | 20.4<small>%</small> | 0.95 | -35.1<small>%</small> | -5.3<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** TQQQ의 CAGR은 43.9%로 QQQ의 19.4%보다 24.5% 높았습니다. (높은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** TQQQ의 표준편차는 60.2%로 QQQ의 20.4%보다 39.9% 높았습니다. (높은 위험도)

**위험도 지표 (MDD):** TQQQ의 81.7%의 MDD는 QQQ의 35.1%보다 46.5% 높았습니다. (높은 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 QQQ의 투자 비중[^fn_vs_weight]을 조절하여 TQQQ의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 20.4% / 60.2% = 296% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 35.1% / 81.7% = 233% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
QQQ<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, QQQ<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![TQQQ](/vs/images/tqqq-vs-qqq.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| TQQQ | <span style="color: tomato">43.9<small>%</small></span> | 60.2<small>%</small> | 0.73 | -81.7<small>%</small> | -19.0<small>%</small> |
| QQQ | <span style="color: tomato">19.4<small>%</small></span> | 20.4<small>%</small> | 0.95 | -35.1<small>%</small> | -5.3<small>%</small> |
| QQQ<sub>STD</sub> <small>(296%)</small> | <span style="color: tomato">49.4<small>%</small></span> | 60.2<small>%</small> | 0.82 | -79.7<small>%</small> | -17.3<small>%</small> |
| QQQ<sub>MDD</sub> <small>(233%)</small> | <span style="color: tomato">41.5<small>%</small></span> | 47.3<small>%</small> | 0.88 | -69.0<small>%</small> | -13.2<small>%</small> |



각각의 경우를 TQQQ의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 296% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 49.4%로 TQQQ의 43.9%보다 5.5% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 233% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 41.5%로 TQQQ의 43.9%보다 -2.4% 낮았습니다. (낮은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 14년 4개월간 거치식으로 투자했다고 가정합니다.

QQQ의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 45.4%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 TQQQ의 43.9%보다 1.5% 높았습니다.

### TQQQ	&lt; QQQ
{: .text-center}


## 관련 정보

- [합성 ETF란 무엇일까? (외주로 맡겨야겠다! 수익률은?)](https://kongdori.tistory.com/255)
- [QQQ가 100% 오르면 TQQQ는 얼마까지 오를 수 있을까?](https://kongdori.tistory.com/188)
- [레버리지 ETF는 위험하다? 위험하지 않다? (위험도와 수익률을 바라보는 관점의 차이)](https://kongdori.tistory.com/182)
- [QLD가 유리할까? QQQ+TQQQ가 유리할까?](https://kongdori.tistory.com/148)
- [TSLL(테슬라 1.5배 레버리지)가 얼마나 올라야 TQQQ(나스닥100 3배 레버리지) 보다 유리할까?](https://kongdori.tistory.com/116)
- [무한매수법과 VR(Value Rebalancing) 수익률에 대한 몇 가지 생각](https://kongdori.tistory.com/109)
- [SQQQ는 TQQQ보다 왜 더 위험한가? (레버리지 ETF 유지 비용을 추산해 봅니다)](https://kongdori.tistory.com/77)
- [TQQQ와 SQQQ를 반반씩 장기 투자하면 어떻게 될까?](https://kongdori.tistory.com/69)
- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}