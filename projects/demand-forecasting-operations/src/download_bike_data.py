"""
Download UCI Machine Learning Repository — Bike Sharing Dataset
Replaces: generate_data.py (synthetic hourly demand data)

DATA SOURCE:
    Fanaee-T, H., & Gama, J. (2013).
    Event labeling combining ensemble detectors and background knowledge.
    Progress in Artificial Intelligence, 2(2-3), 113-127.
    https://doi.org/10.24432/C5W894

DOWNLOAD:
    https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip
    Direct ZIP download, no authentication required.

CITATION:
    @article{fanaee2013event,
      title={Event labeling combining ensemble detectors and background knowledge},
      author={Fanaee-T, Hadi and Gama, João},
      journal={Progress in Artificial Intelligence},
      volume={2},
      number={2-3},
      pages={113--127},
      year={2013},
      publisher={Springer}
    }

DATA DESCRIPTION:
    - day.csv   : Daily bike rental counts (731 days, 2011-2012)
    - hour.csv  : Hourly bike rental counts (17,379 hours, 2011-2012)
    - Features  : season, year, month, hour, holiday, weekday, workingday,
                  weather situation, temperature, feeling temperature,
                  humidity, windspeed, casual users, registered users, total count
"""
import urllib.request
import zipfile
import os


def download_bike_sharing():
    """Download and extract UCI Bike Sharing Dataset."""
    url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00275/Bike-Sharing-Dataset.zip"
    zip_path = "bike_sharing.zip"
    extract_dir = "bike_sharing_data"

    print("📡 Downloading UCI Bike Sharing Dataset...")
    print(f"   Source: {url}")
    print(f"   Citation: Fanaee-T & Gama (2013), Progress in AI, 2(2-3), 113-127")
    print(f"   DOI: https://doi.org/10.24432/C5W894")

    # Download
    urllib.request.urlretrieve(url, zip_path)
    file_size = os.path.getsize(zip_path) / 1024
    print(f"   ✓ Downloaded: {zip_path} ({file_size:.1f} KB)")

    # Extract
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
    print(f"   ✓ Extracted to: {extract_dir}/")

    # Verify files
    for root, dirs, files in os.walk(extract_dir):
        for file in sorted(files):
            if file.endswith('.csv'):
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath) / 1024
                print(f"      📄 {file} ({size:.1f} KB)")

    # Cleanup
    os.remove(zip_path)
    print(f"   ✓ Cleaned up: {zip_path}")

    print("\n📊 DATASET STRUCTURE:")
    print("   - day.csv  → 731 daily records (2011-2012)")
    print("   - hour.csv → 17,379 hourly records (2011-2012)")
    print("   - readme.txt → Full documentation")

    return extract_dir


if __name__ == "__main__":
    data_dir = download_bike_sharing()
    print(f"\n✅ Dataset ready in: {os.path.abspath(data_dir)}")
