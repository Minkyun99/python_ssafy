당신은 시니어 프로젝트 메니저 입니다. 챗봇 서비스 개발을 위한 PRD를 신중히 작성하시오.

<기능 요구 사항>
1. Navbar에는 브랜드 로고(SSAFY)와 채팅, 로그인, 회원가입 버튼을 만드시오.
2. 로고를 클릭하면 서비스를 소개하는 랜딩 페이지로 이동하시오. 
3. 채팅을 클릭하면 AI 채팅 페이지로, 로그인과 회원가입 버튼은 각각 로그인과 회원가입 페이지로 이동하시오.
4. 모던한 디자인으로 화면을 구성하고, 포인트 컬러는 #00EEFF를 사용하시오.
5. 프런트엔드는 React, TypeScript, Styling은 Bootstrap 5.3, Backend는 Node.js로 구현하시오. 
6. 상태관리는 Redux를 사용하시오.
</기능 요구 사항>

<채팅 페이지 상세 요구 사항>
1. 사람이 질문하면 gpt-5-nano 모델이 응답하는 챗봇을 구현하시오.
2. 사람이 질문하는 입령 창은 화면 하단에 고정하고, 왼쪽부터 순서대로 이미지 업로드 버튼, 프롬프트 입력창, 전송 버튼을 만드시오.
3. 사람이 이미지를 업로드하면 이미지 업로드 버튼 위에 미리보기를 출력하고, 미리보기 위에 마우스를 올리면 취소할 수 있는 버튼을 만드시오.
4. 채팅 내역을 출력하는 화면은 우측에 사용자 질문, 좌측에 AI 답변을 출력해 채팅 UI로 구성하시오.
5. 채팅 내역에 사용자가 전송한 이미지도 있을 땐 이미지도 출력하시오.  
6. 반응형 UI를 구현하시오. 
</채팅 페이지 상세 요구 사항>

<작성 시 주의사항>
1. 한글로 작성하시오.
2. PRD를 제외한 다른 말은 하지 마시오.
</작성 시 주의사항>

<gpt-5-nano API 코드 예시>
import OpenAI from "openai";

const openai = new OpenAI();

const response = await openai.responses.create({
    model: "gpt-4.1-mini",
    input: [{
        role: "user",
        content: [
            { type: "input_text", text: "what's in this image?" },
            {
                type: "input_image",
                image_url: "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
            },
        ],
    }],
});

console.log(response.output_text);
</gpt-5-nano API 코드 예시>

<작성 예시>
# Project: My Awesome TypeScript Library

## General Instructions:

- When generating new TypeScript code, please follow the existing coding style.
- Ensure all new functions and classes have JSDoc comments.
- Prefer functional programming paradigms where appropriate.
- All code should be compatible with TypeScript 5.0 and Node.js 20+.

## Coding Style:

- Use 2 spaces for indentation.
- Interface names should be prefixed with `I` (e.g., `IUserService`).
- Private class members should be prefixed with an underscore (`_`).
- Always use strict equality (`===` and `!==`).

## Specific Component: `src/api/client.ts`

- This file handles all outbound API requests.
- When adding new API call functions, ensure they include robust error handling and logging.
- Use the existing `fetchWithRetry` utility for all GET requests.

## Regarding Dependencies:

- Avoid introducing new external dependencies unless absolutely necessary.
- If a new dependency is required, please state the reason.
</작성 예시>