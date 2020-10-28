from pathlib import Path

from app.main import main


def test_main():
    root_dir = Path(__file__).parent.parent
    result_csv = root_dir / 'result.csv'
    if result_csv.exists():
        result_csv.unlink()
    main(root_dir / 'cargo.csv', root_dir / 'trucks.csv')
    assert result_csv.exists()
