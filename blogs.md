---
layout: splash
title: 네이버 블로그와 최근 글 목록
header:
  overlay_image: "/assets/images/report.jpg"
permalink: /blogs/
---

## 블로그 목록

{% for blog in site.blogs %}
  <a href="{{ blog.url }}">{{ blog.title }}</a>
{% endfor %}

{% include commons/footnotes.md %}
