---
layout: single
title: JEPI vs SCHD
excerpt: JEPI의 최근 4년 2개월 CAGR은 12.5%로 SCHD의 15.8%보다 -3.2% 낮았습니다.
header:
  overlay_color: "#333"
  show_overlay_excerpt: false
toc: true
categories:
- vs
keywords: SCHD, JEPI, JEPI SCHD 비교
---

## 비교 상품 소개


JEPI 상품과 SCHD 상품의 성과를 수익률과 위험도로 비교합니다.





{% include commons/vs-notice.md %}

## 지난 성과

두 상품의 성과를 비교할 수 있는 가장 긴 기간은 최근 4년 2개월입니다. 아래는 이 기간의 성과[^fn_vs_perf]를 그래프와 표로 나타낸 것입니다.
그래프 범례에서 괄호안의 퍼센트 수치는 CAGR[^fn_vs_cagr_metric]입니다.

![JEPI](/vs/images/jepi-vs-schd_dual.png){: .align-center}

| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| JEPI | <span style="color: tomato">12.5<small>%</small></span> | 10.4<small>%</small> | 1.20 | -13.7<small>%</small> | -2.2<small>%</small> |
| SCHD | <span style="color: tomato">15.8<small>%</small></span> | 15.7<small>%</small> | 1.00 | -16.8<small>%</small> | -4.1<small>%</small> |

<!-- more -->


성과를 분석하는 전통적인 방법인 수익률과 위험도[^fn_vs_risk]를 살펴봅니다.

**수익률 지표 (CAGR):** JEPI의 CAGR은 12.5%로 SCHD의 15.8%보다 -3.2% 낮았습니다. (낮은 수익률)[^fn_vs_comp]

**위험도 지표 (표준편차):** JEPI의 표준편차는 10.4%로 SCHD의 15.7%보다 -5.3% 낮았습니다. (낮은 위험도)

**위험도 지표 (MDD):** JEPI의 13.7%의 MDD는 SCHD의 16.8%보다 -3.1% 낮았습니다. (낮은 위험도)



## 동일 수준 위험 노출을 위한 비중 조절

수익률과 위험도가 다른 상품을 비교하는 방법의 하나는, 둘 중 하나를 동일하게 설정하고, 나머지 하나를 비교하는 것입니다.
여기서는 SCHD의 투자 비중[^fn_vs_weight]을 조절하여 JEPI의 위험도와 유사하게 맞추어 수익률를 비교합니다.

**위험도 지표 (표준편차):** 표준편차를 동일한 값으로 맞추기 위해서는 15.7% / 10.4% = 66% 비중으로 투자하면 됩니다.[^fn_vs_sharpe]

**위험도 지표 (MDD):** MDD를 동일한 값으로 맞추기 위해서는 16.8% / 13.7% = 81% 비중으로 투자하면 됩니다.


{% include /commons/ads/adsense.html %}



## 동일 수준 위험하에서의 추정 성과

아래는 비중을 조절한 경우를 추가하여, 그래프와 표에 성과를 기록한 것입니다.
SCHD<sub>STD</sub>는 표준편차를 맞춘[^fn_vs_weighting] 경우이고, SCHD<sub>MDD</sub>는 MDD를 맞춘 경우입니다.
앞에서와 같이 그래프 범례에서 괄호안의 퍼센트 수치는 CAGR입니다.


![JEPI](/vs/images/jepi-vs-schd.png){: .align-center}



| **종목** | **CAGR** | **편차** | **샤프** | **MDD** | **AvDD** |
| :------------ | ------: | -----------: | -------: | ------: | -------: |
| JEPI | <span style="color: tomato">12.5<small>%</small></span> | 10.4<small>%</small> | 1.20 | -13.7<small>%</small> | -2.2<small>%</small> |
| SCHD | <span style="color: tomato">15.8<small>%</small></span> | 15.7<small>%</small> | 1.00 | -16.8<small>%</small> | -4.1<small>%</small> |
| SCHD<sub>STD</sub> <small>(66%)</small> | <span style="color: tomato">10.5<small>%</small></span> | 10.4<small>%</small> | 1.01 | -11.3<small>%</small> | -2.6<small>%</small> |
| SCHD<sub>MDD</sub> <small>(81%)</small> | <span style="color: tomato">12.9<small>%</small></span> | 12.8<small>%</small> | 1.00 | -13.8<small>%</small> | -3.2<small>%</small> |



각각의 경우를 JEPI의 성과와 비교해 봅니다.

**위험도 지표 (표준편차):** 66% 투자 비중으로 표준편차를 비슷한 수준으로 맞추면, CAGR은 10.5%로 JEPI의 12.5%보다 -2.1% 낮았습니다. (낮은 수익률)

**위험도 지표 (MDD):** 81% 투자 비중으로 하여 MDD를 비슷한 수준으로 맞추면, CAGR은 12.9%로 JEPI의 12.5%와 비슷했습니다. (비슷한 수익률)




## 최종 비교

**주의** 투자 시점과 기간, 그리고 전략에 따라 다른 결과가 나올 수 있습니다. 백테스트 기간이 짧은 경우 통계적 신뢰성이 떨어질 수 있습니다. 미래에도 동일한 경향이 지속된다고 보장할 수 없습니다.
{: .notice--warning}

지난 4년 2개월간 거치식으로 투자했다고 가정합니다.

SCHD의 투자 비중을 조절하여 표준편차나 MDD를 동일하게 맞추면, CAGR이 평균 11.7%인 포트폴리오를 만들 수 있습니다.
이 포트폴리오는 JEPI의 12.5%와 비슷했습니다.

### JEPI ≒ SCHD
{: .text-center}
**참고** 위험 대비 수익률이 비슷한 경우라면, 적은 비중으로 동일한 투자 효과를 낼 수 있는 상품을 선택하는 것이, 투자 전략 유연성 측면에서는 보다 유리할 수 있습니다.
{: .notice--info}


## 관련 정보

- [SPY로 JEPI처럼 분배금을 만들면 얼마나 남을까? (기초 자산에서 커버드콜 ETF의 분배금만큼 꺼내 써 보자!)](https://kongdori.tistory.com/284)
- [ISPY - ProShares의 초단기 콜옵션 전략 기반 인컴 ETF (넌 누굴 닮았니?)](https://kongdori.tistory.com/267)
- [커버드콜 ETF는 왜 장기 투자에 적합하지 않은가? (효율적 투자선과 50% 오렌지 주스)](https://kongdori.tistory.com/244)
- [JEPI/JEPQ에 장기 배당 재투자하는 것은 좋은 방법일까? (장기투자와 세금)](https://kongdori.tistory.com/216)
- [당신이 JEPI/JEPQ를 사면 안되는 이유 (해외 상장 인컴 ETF의 배당소득세와 양도소득세)](https://kongdori.tistory.com/213)
- [JEPI/JEPQ는 특별한가? (SCHD/QQQ + 현금과의 비교)](https://kongdori.tistory.com/211)
- [JEPI는 SPY보다 더 좋은 ETF인가? (현금 흐름 창출과 배당 재투자 시)](https://kongdori.tistory.com/183)
- [커버드 콜 전략은 유용한가? (커버드 콜 전략을 쓰는 주요 ETF의 지금까지 수익률과 분석)](https://kongdori.tistory.com/155)
- [JEPI는 매달 현금 흐름이 필요한 경우 현명한 선택이었을까? (SCHD와 비교)](https://kongdori.tistory.com/49)
- [유사 종목 성과 비교 목록](/vs/){: .btn .btn--info}

{% include commons/footnotes.md %}