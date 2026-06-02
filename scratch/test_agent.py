import os
from pathlib import Path
from src.agent.graph import build_agent
from dotenv import load_dotenv

load_dotenv()

agent = build_agent(
    provider="google",
    today="2026-06-01",
)

query = "Tạo đơn hàng cho Nguyễn Lan Anh, số điện thoại 0901234567, email lananh@example.com, giao đến 18 Nguyễn Huệ, Quận 1, TP.HCM. Tôi cần 1 ASUS ROG Zephyrus G14, 2 Logitech Pebble 2 M350s và 1 LG UltraGear 27GP850-B."

response = agent.invoke({"messages": [{"role": "user", "content": query}]})
messages = response["messages"] if isinstance(response, dict) else response

for i, msg in enumerate(messages):
    print(f"[{i}] {msg.__class__.__name__}: {msg.content}")
    if getattr(msg, "tool_calls", None):
        print(f"    Tool Calls: {msg.tool_calls}")
