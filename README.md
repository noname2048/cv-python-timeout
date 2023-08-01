# 💡 동기

직접 구현한 알고리즘과, 솔루션으로 구현된 풀이가 **같은 답을 내놓는지 테스트**하고 있었습니다. 테스트 방법으로 두 개의 알고리즘에 **무작위**로 만든 무제들을 넣어 답이 같은지 확인하였지만, 몇 개의 테스트케이스가 **무한루프**에 빠졌습니다.
이 경우에 **시간초과시 무시**하고 나머지 테스트를 진행하게 하고 싶었습니다. 백준, 프로그래머스 등의 알고리즘 풀이 사이트에서도 **timeout** 을 구현해 놓았을 텐데, 어떤식으로 구현했는지 알아보는 중에 시그널을 사용하는 **해답**을 찾았습니다.
해답은 **데코레이터**와 **시그널**을 이용했는데, 평소 이용하는 데코레이터 형식과 달라 이해하는데 많은 **시간**이 걸렸습니다. 
공부하고 나니 데코레이터를 잘 이해하지 못하고 있어서 오래걸렸던 것을 알아차렸습니다. 그래서 데코레이터에 조금 더 치중한 풀이가 되었지만, 파이썬을 **이해**하는데 도움이 되었습니다.

공부하다 보니 정성들여 쓴 글을 보며 도움을 받았습니다. **비슷한** 내용의 글을 **하위**버전으로 쓸까봐 글을 게제하지 않으려고 했지만, 어쩌다보니 방향성이 조금 다른 글이 되어 기재합니다. 다른 분들에게도 **도움**이 되면 좋겠습니다.

---

문제의 **발단**이 된 블로그:
- tistory(쌀 팔다 개발자): [python 함수 timeout 설정하기](https://daeguowl.tistory.com/139)
- ⭐️ **programmers community**: [함수가 완료되는데에 너무 오래걸릴 때, timeout시키기](https://qna.programmers.co.kr/questions/2203/%ED%95%A8%EC%88%98%EA%B0%80-%EC%99%84%EB%A3%8C%EB%90%98%EB%8A%94%EB%8D%B0%EC%97%90-%EB%84%88%EB%AC%B4-%EC%98%A4%EB%9E%98-%EA%B1%B8%EB%A6%B4-%EB%95%8C-timeout%EC%8B%9C%ED%82%A4%EA%B8%B0) 

좋은 내용이 있던 블로그:
- 👍 velog(@doondoony): [Python functools.wraps 를 알아보자](https://velog.io/@doondoony/python-functools-wraps)
- velog(@kmp1007s): [함수형 프로그래밍의 Currying](https://velog.io/@kmp1007s/%ED%95%A8%EC%88%98%ED%98%95-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D%EC%9D%98-Currying)

## 👀 파일설명

- 00_problem : 🤔 어떻게 동작하는지 이해하고 싶은 코드 조각(**발단**) 
- 01_simple_decorator: 😄 해당 방법의 데코레이터만 알고 있어서 00을 이해하는데 오래걸렸습니다. (이해가 **오래**걸린 원인) 
- 02_update_wrapper: wraps를 이해하기 앞서 **update_wrapper** 을 이해해봅니다.
- 03_partial: wraps를 이해하기 앞서 **partial** 을 이해해봅니다.
- 04_args_kwargs: parital 을 **좀 더** 이해하기 위해 positial args, args, keword args 에 대해 살펴봅니다.
- 05_wraps:  **wraps** 를 이해하고 함수형 프로그래밍의 **currying** 기능도 사용해 봅니다.
- 06_decorator_in_func: 데코레이터를 좀 더 자세하게 살펴봅니다. 여러개의 함수가 **중첩**된 것처럼 보이는 데코레이터를 사용해봅니다.
- 07_callable_or_not: 데코레이터를 사용하는 **2가지 방식**에 한거번에 대응하는 데코레이터를 만들어 봅니다.
- 08_signal: **signal**을 간략하게 사용해봅니다.
- 09_signal_decorator: 🙌 signal을 사용한 decorator 를 **이해**합니다. 