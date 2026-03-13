from app.domain.services.nf_parser_service import NfParserService


def test_should_append_continuation_with_text():
    service = NfParserService()
    assert service.should_append_continuation("CONTINUAÇÃO PRODUTO 123")