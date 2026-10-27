// 다른 사이트가 이 페이지를 틀(iframe) 안에 넣으면 이 페이지로 바로 빠져나와요 (클릭재킹 막기)
if (window.top !== window.self) { window.top.location.replace(window.self.location.href); }
