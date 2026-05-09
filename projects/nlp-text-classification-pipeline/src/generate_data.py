"""
Synthetic text classification data generator.
Creates realistic public-sector documents based on real-world patterns.

Categories mirror:
- FOIA requests (MuckRock patterns)
- DC 311 service requests
- Federal Register notices
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import os


# Realistic document templates for each category
FOIA_TEMPLATES = [
    "Request for records related to {topic} under the Freedom of Information Act. Seeking documents from {date_range} including emails, memos, and reports.",
    "Pursuant to FOIA, I request all documents concerning {topic} prepared between {date_range}. Please include drafts and internal correspondence.",
    "Under the Freedom of Information Act, 5 U.S.C. § 552, I request access to records regarding {topic} from {agency} for the period {date_range}.",
    "FOIA request for {topic} records. Specifically seeking: budgets, expenditures, contracts, and correspondence related to this matter from {date_range}.",
    "Requesting disclosure of all records pertaining to {topic} maintained by {agency}. Time period: {date_range}. Please expedite if possible.",
]

SERVICE_TEMPLATES = [
    "Rodent complaint at {address}. Multiple sightings reported in basement and alley. Request extermination services.",
    "Pothole repair needed at {address}. Large pothole causing vehicle damage and safety hazard for cyclists.",
    "Illegal dumping observed at {address}. Construction debris and household waste accumulating for over a week.",
    "Street light outage at {address}. Complete darkness on block creating safety concerns for pedestrians.",
    "Tree down blocking roadway at {address}. Storm damage from last night. Emergency removal needed.",
    "Water main break at {address}. Flooding street and sidewalk. Low water pressure in surrounding area.",
    "Graffiti removal request at {address}. Multiple tags on public building facade.",
    "Abandoned vehicle at {address}. White sedan, no plates, parked for 3+ weeks.",
    "Noise complaint: loud construction at {address} before 7 AM on weekday.",
    "Sidewalk repair needed at {address}. Uneven surface creating tripping hazard for elderly residents.",
]

POLICY_TEMPLATES = [
    "Notice of proposed rulemaking regarding {topic}. Comments accepted through {deadline}. Public hearing scheduled.",
    "Final rule amending regulations for {topic}. Effective date {deadline}. Compliance required within 90 days.",
    "Advance notice of proposed rulemaking: seeking public input on {topic}. Comment period {date_range}.",
    "Interim final rule with request for comments on {topic}. Effective immediately. Comments due {deadline}.",
    "Notice of information collection under review: {topic}. OMB control number renewal requested.",
    "Request for information regarding {topic}. Agency seeking data and feedback from stakeholders.",
    "Notice of availability: draft environmental impact statement for {topic}. Public comment period {date_range}.",
    "Direct final rule amending {topic} without objection. Effective {deadline} unless adverse comments received.",
]

BUDGET_TEMPLATES = [
    "FY{year} budget request for {topic}. Total allocation: ${amount}. Breakdown: personnel ${personnel}, equipment ${equipment}, contracts ${contracts}.",
    "Supplemental appropriation request: {topic}. Emergency funding needed due to {reason}. Amount: ${amount}.",
    "Quarterly expenditure report for {topic}. Spent: ${spent} of ${allocated} budget. Variance: {variance}%.",
    "Grant award notification: {topic}. Award amount ${amount}. Performance period: {date_range}.",
    "Contract modification request for {topic}. Increase scope by ${amount}. Justification: {reason}.",
    "Budget reprogramming notification: ${amount} transferred from {source} to {topic}. Approved by {approver}.",
]

TOPICS = [
    "transit infrastructure maintenance", "public health surveillance", "emergency response protocols",
    "environmental compliance", "workforce development programs", "digital service delivery",
    "affordable housing initiatives", "climate adaptation planning", "public safety technology",
    "education funding allocation", "small business support", "veterans services",
    "community health centers", "food security programs", "transportation equity"
]

AGENCIES = [
    "Department of Transportation", "Department of Health", "Office of Emergency Management",
    "Environmental Protection Agency", "Department of Labor", "General Services Administration",
    "Department of Housing", "Department of Education", "Small Business Administration",
    "Department of Veterans Affairs", "Department of Agriculture", "Federal Transit Administration"
]

ADDRESSES = [
    "1234 K Street NW", "5678 14th Street SE", "9012 Georgia Avenue", 
    "3456 Pennsylvania Ave", "7890 Constitution Ave", "2345 Massachusetts Ave",
    "6789 Connecticut Ave", "123 H Street NE", "456 U Street NW", "789 7th Street SW"
]


def generate_documents(n_docs=2000, random_state=42):
    """Generate synthetic public-sector documents."""
    np.random.seed(random_state)
    
    docs = []
    categories = ['FOIA', 'Service_Request', 'Policy', 'Budget']
    
    for i in range(n_docs):
        cat = np.random.choice(categories, p=[0.15, 0.35, 0.25, 0.25])
        topic = np.random.choice(TOPICS)
        agency = np.random.choice(AGENCIES)
        address = np.random.choice(ADDRESSES)
        
        date_range = f"{np.random.randint(2020, 2024)}-{np.random.randint(2020, 2024)}"
        deadline = (datetime(2024, 1, 1) + timedelta(days=np.random.randint(0, 365))).strftime("%B %d, %Y")
        year = np.random.randint(2023, 2026)
        amount = f"{np.random.randint(100, 5000):,}"
        
        if cat == 'FOIA':
            template = np.random.choice(FOIA_TEMPLATES)
            text = template.format(topic=topic, date_range=date_range, agency=agency)
        elif cat == 'Service_Request':
            template = np.random.choice(SERVICE_TEMPLATES)
            text = template.format(address=address)
        elif cat == 'Policy':
            template = np.random.choice(POLICY_TEMPLATES)
            text = template.format(topic=topic, deadline=deadline, date_range=date_range)
        else:  # Budget
            template = np.random.choice(BUDGET_TEMPLATES)
            text = template.format(
                topic=topic, year=year, amount=amount,
                personnel=f"{np.random.randint(50, 2000):,}",
                equipment=f"{np.random.randint(20, 800):,}",
                contracts=f"{np.random.randint(30, 1500):,}",
                spent=f"{np.random.randint(100, 4000):,}",
                allocated=f"{np.random.randint(100, 5000):,}",
                variance=np.random.randint(-20, 20),
                reason=np.random.choice(["cost overrun", "scope expansion", "emergency need", "funding gap"]),
                source=np.random.choice(TOPICS),
                approver=np.random.choice(["CFO", "Budget Director", "Program Manager", "Deputy Mayor"]),
                date_range=date_range
            )
        
        docs.append({
            'doc_id': f'DOC-{i:05d}',
            'category': cat,
            'text': text,
            'created_date': datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 730)),
            'agency': agency if cat != 'Service_Request' else 'DC 311',
            'word_count': len(text.split()),
            'has_attachment': np.random.choice([True, False], p=[0.3, 0.7]),
            'priority': np.random.choice(['Low', 'Medium', 'High', 'Urgent'], p=[0.2, 0.4, 0.3, 0.1])
        })
    
    return pd.DataFrame(docs)


def main():
    """Generate datasets and save."""
    out_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(out_dir, '..', 'data')
    os.makedirs(data_dir, exist_ok=True)
    
    print("Generating public-sector documents...")
    docs = generate_documents(n_docs=2000)
    docs.to_csv(os.path.join(data_dir, 'documents.csv'), index=False)
    print(f"  Saved {len(docs)} documents")
    
    # Also generate a smaller labeled test set
    test_docs = generate_documents(n_docs=500, random_state=99)
    test_docs.to_csv(os.path.join(data_dir, 'test_documents.csv'), index=False)
    print(f"  Saved {len(test_docs)} test documents")
    
    print("\nDone!")


if __name__ == '__main__':
    main()
