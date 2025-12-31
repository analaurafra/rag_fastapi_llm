from ai_service import generate_text


def test_generate_text_returns_mock_when_no_key():
    # Ensure mocked path returns predictable string when OPENAI_API_KEY is not set
    out = generate_text("test prompt")
    assert isinstance(out, str)
    assert "MOCKED RESPONSE" in out
