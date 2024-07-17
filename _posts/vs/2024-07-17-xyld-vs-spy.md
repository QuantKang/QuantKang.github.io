---
layout: single
title: XYLD vs SPY
excerpt: XYLD의 최근 11년 1개월 CAGR은 5.7%로 SPY의 14.1%보다 -8.5% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: SPY, XYLD, XYLD SPY 비교
---

## 비교 상품 소개


S&P 500 지수에 대해 커버드 콜 전략을 쓰는 XYLD와 S&P 500 지수를 추종하는 SPY의 성과를 비교해 봅니다.



{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 11년 1개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.

![XYLD](/vs/images/xyld-vs-spy_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| XYLD | <span style="color: tomato">5.7<small>%</small></span> | 13.9<small>%</small> | 0.41 | -34.7<small>%</small> | -4.7<small>%</small> |
| SPY | <span style="color: tomato">14.1<small>%</small></span> | 16.9<small>%</small> | 0.84 | -33.7<small>%</small> | -4.0<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** XYLD의 CAGR은 5.7%로 SPY의 14.1%보다 -8.5% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** XYLD의 표준편차는 13.9%로 SPY의 16.9%보다 -3.0% 낮았습니다. (낮은 위험도)

**위험도 지표 (MDD):** XYLD의 34.7%의 MDD는 SPY의 33.7%와 비슷했습니다. (비슷한 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 SPY의 투자 비중[^fn_vs_weight]을 조절하여 XYLD의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 16.9% / 13.9% = 82% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 33.7% / 34.7% = 103% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
SPY<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, SPY<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![XYLD](/vs/images/xyld-vs-spy.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| XYLD | <span style="color: tomato">5.7<small>%</small></span> | 13.9<small>%</small> | 0.41 | -34.7<small>%</small> | -4.7<small>%</small> |
| SPY | <span style="color: tomato">14.1<small>%</small></span> | 16.9<small>%</small> | 0.84 | -33.7<small>%</small> | -4.0<small>%</small> |
| SPY<sub>STD</sub> <small>(82%)</small> | <span style="color: tomato">11.7<small>%</small></span> | 13.9<small>%</small> | 0.84 | -28.4<small>%</small> | -3.3<small>%</small> |
| SPY<sub>MDD</sub> <small>(103%)</small> | <span style="color: tomato">14.5<small>%</small></span> | 17.4<small>%</small> | 0.84 | -34.6<small>%</small> | -4.2<small>%</small> |



각각의 경우를 XYLD의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 82% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 11.7%로 XYLD의 5.7%보다 6.0% 높았습니다. (높은 수익률)

**위험도 지표 (MDD):** 103% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 14.5%로 XYLD의 5.7%보다 8.8% 높았습니다. (높은 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 11년 1개월간 거치식으로 투자했다고 가정합니다.

SPY의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 13.1%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 XYLD의 5.7%보다 7.4% 높았습니다.

### XYLD	&lt; SPY
{: .text-center}


## 관련 정보

- [커버드콜 ETF 대신 기초 자산으로 현금 흐름을 만들면? (시장 대표 지수편)](https://kongdori.tistory.com/285)
- [ISPY - ProShares의 초단기 콜옵션 전략 기반 인컴 ETF (넌 누굴 닮았니?)](https://kongdori.tistory.com/267)
- [TIGER 미국배당+7%프리미엄다우존스의 수익률은 왜 좋지 못했을까? (커버드콜 ETF를 수식으로 표현해 보자!)](https://kongdori.tistory.com/264)
- [BALI - 블랙록의 커버드콜 기반 인컴 ETF (발리섬에서 은퇴 생활을 즐길 수 있을까? JEPQ의 S&P500 버전)](https://kongdori.tistory.com/261)
- [KODEX 미국S&P500배당귀족커버드콜(합성 H) (장기 수익률에 안 좋은 건 다 넣었어요. 맛있게 드세요.)](https://kongdori.tistory.com/258)
- [JEPI - CALL = ? (JEPI/JEPQ의 내부는 어떤 액티브 ETF일까?)](https://kongdori.tistory.com/256)
- [커버드콜 ETF는 왜 장기 투자에 적합하지 않은가? (효율적 투자선과 50% 오렌지 주스)](https://kongdori.tistory.com/244)
- [커버드콜은 정말 하락장과 횡보장에 유리할까?](https://kongdori.tistory.com/238)
- [커버드 콜 전략은 유용한가? (커버드 콜 전략을 쓰는 주요 ETF의 지금까지 수익률과 분석)](https://kongdori.tistory.com/155)
- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}