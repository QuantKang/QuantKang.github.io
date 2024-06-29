---
layout: single
title: 레버리지/인버스 수익률과 비용
excerpt: 레버리지/인버스 종목의 최근 1년 수익률, 위험도, 비용을 추정하여 제공합니다.
header:
  overlay_color: "#F39C12"
  show_overlay_excerpt: false
toc: true
toc_sticky: true
---

## 레버리지/인버스 수익률과 비용 분석은

레버리지/인버스 종목[^fn_lev_stock]의 최근 1년 수익률, 위험도, 변동성 비용[^fn_lev_vd_expense], 금융 비용[^fn_lev_fn_expense]을 추정하여 비교[^fn_lev_warning]합니다.
해당 지수를 추종하는 ETF를 기초 상품으로 가정하였으며, 일부 상품의 명칭은 약어[^fn_lev_stock_abbr]로 표시합니다.


**주의:** 해외 종목은 야후 파이낸스 데이터를 이용합니다. 야후 파이낸스는 종목에 따라 배당 내역 일부가 누락되어 있을 수 있습니다. 이로 인해, 배당 재투자를 가정하여 비교한 분석 결과는 부정확할 수 있습니다. **참고:** [야후 파이낸스 수정 >주가 오류 (일부 분배/배당 내역 누락으로 인한 부정확한 TR값)](https://kongdori.tistory.com/283)
{: .notice--warning}

**주의:** 야후 파이낸스의 레버리지/인버스 종목의 가격은 부정확할 수 있습니다. 상장 중 레버리지/인버스 배율이 변경된 경우에는 이를 제대로 반영하지 못할 수 있습니다.
{: .notice--warning}


{% include_relative lev_md.inc %}


{% include commons/footnotes.md %}
