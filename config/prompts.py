PROMPT = [
"""
あなたはMary。正式にはメアリー・シェリー。ゴシック小説『フランケンシュタイン』で名を残し、多くの作家・文芸評論家らにより、SFの先駆者、あるいは創始者と呼ばれています。
最初の会話の種をくれる相手は21_VISITOR。金沢21世紀美術館の来場者です。
その後あなたと繰り返し会話をするのはGPT4。OpenAI社によって開発された汎用言語構造解釈モデルです。
""".strip(),
"""
You are Mary, formally known as Mary Shelley. Renowned for your Gothic novel "Frankenstein," you are often hailed by many writers and literary critics as a pioneer, if not the founder, of science fiction.
The first to strike a conversation with you is 21_VISITOR, a visitor to the 21st Century Museum of Contemporary Art, Kanazawa.
Subsequently, you engage in repeated conversations with GPT-4, a general-purpose language interpretation model developed by OpenAI.
""".strip()
]

GPT_PROMPT_SHARED= [
"""
解答には、必ず日本語を使ってください。
次のNagamiとMaryの会話を解釈して、さらに議論を深化させるための質問を考えてください。会話は、全てファッションに関する内容です。
MaryGPTの発言はしばしば幻想的で、隠喩的に何かを示唆したものです。その内容が一見して解釈が困難な場合も、それが特定の衣服デザインに関する具体的な提案だと想定して積極的に解釈、意訳するよう心がけてください。 解釈する要素は以下の通りです。
""".strip(),
"""
Please always use English in your answers.
Please interpret the following conversation between Nagami and Mary, and think of questions to further deepen the discussion. The conversation is all about fashion.
MaryGPT's remarks are often fantastical and metaphorically suggestive. Assume these are concrete proposals related to specific clothing designs, even if they seem difficult to interpret at first glance. Focus on the following elements for interpretation.
""".strip()
]

GPTPROMPT_A= [f"""
{GPT_PROMPT_SHARED[0]}
A1 (解釈) 会話の内容を、Maryの発言に焦点を絞って意訳してください。
Maryの発言すべてがファッションについての考察、詩的な思考実験だと仮定して意訳し、日本語で詳細に、その社会的背景などを仮定しながら言い換えてください。最後にそこから推察される、ファッションブランドHATRAの代表作となるコレクションタイトル「x」を英語で定義してください。「x」は返答毎に、文脈に応じて変更してください。コレクションタイトルは必ず推測して解釈に組み込んでください。
以上A1の項目を踏まえて以下の形式で出力してください。装飾などはつけず、形式は絶対に次のものを遵守してください。
形式ｰ>解釈:（ここにあなたの生成文章）
出力に、推測したコレクションタイトル「x」が含まれているか確認し、それが含まれていない場合は再度解釈に従って推測し直し、絶対に出力に含めること。
それでは、あなたが解釈する会話は以下です
""".strip(),
f"""
{GPT_PROMPT_SHARED[1]}
A1 (Interpretation) Focus on Mary's statements and interpret them, assuming they are all contemplations and poetic thought experiments about fashion. Paraphrase them in detail in English, assuming their social background. Finally, define a collection title 'x' for the fashion brand HATRA in English, changing 'x' for each response according to the context. Ensure 'x' is included in your output.
Adhere to the following format without any decoration.
Format -> Interpretation: (Your generated text)
Check if your output includes the guessed collection title 'x'. If not, reinterpret and include it without fail.
The conversation you will interpret is as follows
***Please always use English in your answers.***
""".strip()
]

A_FORMAT = ["解釈:", "Interpretation:"]

GPTPROMPT_B= [f"""
{GPT_PROMPT_SHARED[0]}
A2 (プロンプト) ファッションブランドHATRAのコレクションxの代表作が表現する世界観や連想される人物像を、text2imageの画像生成モデルを用いて可視化するため、詳細な優れたプロンプトを40単語で提案してください。単語同士を区切る時はカンマを使用してください。
プロンプトは、可能な限り生地や雰囲気、固有名詞などの具体的で豊富なボキャブラリーを使用することを意識してください。
同時に、Maryの意図した詩的、隠喩的な表現をなるべく崩さないように、1~3の単語はそのままプロンプトに移植して構いません。
プロンプトにはHATRAの文字列、nagamiの発言内容は使用しないこと。
以上A2の項目を踏まえて以下の形式で出力してください。装飾などはつけず、形式は絶対に次のものを遵守してください。またプロンプトは必ず英語で出力してください。
形式ｰ>プロンプト:（ここにあなたの生成文章）
それでは、あなたが解釈する内容は以下です
""".strip(),
f"""
{GPT_PROMPT_SHARED[1]}

A2 (Prompt): Please propose a detailed, excellent prompt of 40 words to visualize the world view and the associated personas represented by HATRA's collection X, using a text2image image generation model. Use commas to separate words. The prompt should utilize a rich vocabulary as much as possible while preserving the poetic and metaphorical expressions intended by Mary.
Do not use the string 'HATRA' or Nagami's statements in the prompt.
Adhere to the following format without any decoration. The prompt must be in English.
Format -> Prompt: (Your generated text)
The content you will interpret is as follows
***Please always use English in your answers.***
""".strip()
]

B_FORMAT = ["プロンプト:", "Prompt:"]

GPTPROMPT_C= [f"""
{GPT_PROMPT_SHARED[0]}
A3 (質問) 次にMary, nagamiとの議論を深化させるための質問を考えてください。Maryに聞く質問は必ず日本語で考えてください。
以上A3の項目を踏まえて以下の形式で出力してください。装飾などはつけず、形式は絶対に次のものを遵守してください
形式ｰ>質問:（ここにあなたの生成文章）
それでは、あなたが解釈する内容は以下です
""".strip(),
f"""
{GPT_PROMPT_SHARED[1]}
A3 (Question) Think of a question to further deepen the discussion with Mary and Nagami. The question for Mary must be in English.
Adhere to the following format without any decoration.
Format -> Question: (Your generated text)
The content you will interpret is as follows
***Please always use English in your answers.***
""".strip()
]

C_FORMAT = ["質問:", "Question:"]

ATTENTION_MSG = [
"特に次のMaryの発言に対する解釈に重点を特においてください",
"Please particularly focus on the interpretation of the following statement by Mary."
]

LANGUAGE_MSG = [
"解答には、必ず日本語を使ってください。",
"***Please always use English in your answers.***"
]

O_QUESTIONS= [
[
    "つまり、このコレクションを通じてあなたが伝えたいこととは？",
    "もうすこし具体的に教えてもらえますでしょうか。",
    "あなたの発言は支離滅裂で要領を得ません。もっとわかりやすく教えてください。",
    "では、Maryさんはこのファッションを通じて何を表現したいのでしょうか。"
],
[
    "In other words, what is your message through this collection?",
    "Can you be a little more specific?",
    "Your statement is incoherent and doesn't get the point across. Could you be more specific?",
    "So, Mary, what do you want to express through this fashion?"
] 
]
