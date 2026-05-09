"""
Synthetic data generator for NLP text classification pipeline.
Creates realistic public-sector documents with real-world patterns.
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed for reproducibility
random.seed(42)
np.random.seed(42)


# Government document templates based on real patterns
templates = {
    'FOIA': [
        "I am requesting access to {topic} records under the Freedom of Information Act. "
        "Specifically, I need {document_type} related to {agency} from {date_range}.",
        "Pursuant to 5 U.S.C. § 552, I request copies of all {document_type} concerning {topic}. "
        "Please provide responsive documents in electronic format.",
        "Under the FOIA, I am seeking records regarding {topic} maintained by {agency}. "
        "This request includes emails, memoranda, and reports from {date_range}."
    ],
    'Service_Request': [
        "Complaint: {issue_type} at {location}. Resident reports {description}. "
        "Priority: {priority}. Contact: {contact_info}.",
        "Service needed: {issue_type} reported at {location}. {description}. "
        "Please dispatch maintenance crew {priority}.",
        "Urgent: {issue_type} causing {description} at {location}. "
        "Multiple residents affected. Request immediate response."
    ],
    'Policy': [
        "Notice of Proposed Rulemaking: {topic}. {agency} proposes to amend regulations "
        "regarding {topic}. Public comment period ends {date_range}.",
        "Final Rule: {topic}. Effective date {date_range}. This rule establishes "
        "standards for {topic} under authority of {statute}.",
        "Policy Memorandum: Implementation guidance for {topic}. All {agency} units "
        "must comply by {date_range}. Contact {contact_info} for questions."
    ],
    'Budget': [
        "FY{year} Budget Allocation: {category} funding request of ${amount}. "
        "Justification: {justification}. Previous year actual: ${previous_amount}.",
        "Expenditure Report: {category} spent ${amount} in Q{quarter}. "
        "Variance from budget: {variance}%. {justification}.",
        "Grant Application: {agency} requests ${amount} for {topic}. "
        "Project period: {date_range}. Expected outcomes: {justification}."
    ]
}


topics = [
    "transit operations", "public safety", "waste management", "street maintenance",
    "public health", "environmental compliance", "facilities management",
    "IT infrastructure", "human resources", "financial auditing"
]

agencies = [
    "DOT", "DPW", "DHS", "DOH", "DGS", "OCP", "CFO", "OMB", "HR"
]

issue_types = [
    "pothole repair", "street light outage", "graffiti removal", "rodent control",
    "sidewalk repair", "traffic signal malfunction", "water main break",
    "tree removal", "illegal dumping", "noise complaint"
]

locations = [
    "123 Main St", "5th & Broadway", "Central Park area", "District 3",
    "Riverside Community Center", "Downtown Corridor", "Northwest Sector"
]


def generate_document(category, doc_id):
    """Generate a single synthetic document."""
    template = random.choice(templates[category])
    
    year = random.choice([2023, 2024])
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    
    context = {
        'topic': random.choice(topics),
        'agency': random.choice(agencies),
        'date_range': f"{month}/{day}/{year} to {month+1}/{day}/{year}",
        'document_type': random.choice(["memoranda", "emails", "reports", "contracts"]),
        'issue_type': random.choice(issue_types),
        'location': random.choice(locations),
        'description': random.choice([
            "ongoing for 3 days", "first reported last week", "multiple complaints received",
            "emergency situation", "routine maintenance needed"
        ]),
        'priority': random.choice(['low', 'medium', 'high', 'urgent']),
        'contact_info': f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}",
        'year': year,
        'category': random.choice(["Operations", "Capital", "Personnel", "Maintenance", "Technology"]),
        'amount': f"{random.randint(50, 5000)}K",
        'previous_amount': f"{random.randint(40, 4500)}K",
        'justification': random.choice([
            "Critical infrastructure needs", "Regulatory compliance requirement",
            "Population growth demands", "Equipment replacement cycle",
            "Safety improvement initiative"
        ]),
        'quarter': random.choice([1, 2, 3, 4]),
        'variance': random.randint(-20, 30),
        'statute': random.choice(["42 U.S.C. § 7401", "23 U.S.C. § 101", "49 U.S.C. § 5301"])
    }
    
    text = template.format(**context)
    
    # Add some random variation
    if random.random() < 0.3:
        text += f" Additional context: {random.choice(topics)}."
    
    return {
        'doc_id': doc_id,
        'category': category,
        'text': text,
        'created_date': datetime(year, month, day),
        'word_count': len(text.split()),
        'priority': context['priority'] if category == 'Service_Request' else random.choice(['low', 'medium', 'high']),
        'has_attachment': random.random() < 0.4,
        'source_agency': context['agency']
    }


def generate_dataset(n_documents=2000, output_dir='../data'):
    """Generate full synthetic dataset."""
    # Category distribution (realistic for government docs)
    categories = ['FOIA', 'Service_Request', 'Policy', 'Budget']
    weights = [0.10, 0.35, 0.25, 0.30]
    
    documents = []
    for i in range(n_documents):
        category = random.choices(categories, weights=weights)[0]
        doc = generate_document(category, f"DOC_{i:05d}")
        documents.append(doc)
    
    df = pd.DataFrame(documents)
    
    # Sort by date
    df = df.sort_values('created_date').reset_index(drop=True)
    
    # Save
    df.to_csv(f'{output_dir}/documents.csv', index=False)
    print(f"Generated {len(df)} documents")
    print(f"Category distribution:")
    print(df['category'].value_counts())
    
    return df


def generate_test_set(n_documents=500, output_dir='../data'):
    """Generate test dataset with similar distribution."""
    categories = ['FOIA', 'Service_Request', 'Policy', 'Budget']
    weights = [0.10, 0.35, 0.25, 0.30]
    
    documents = []
    for i in range(n_documents):
        category = random.choices(categories, weights=weights)[0]
        doc = generate_document(category, f"TEST_{i:05d}")
        documents.append(doc)
    
    df = pd.DataFrame(documents)
    df.to_csv(f'{output_dir}/test_documents.csv', index=False)
    print(f"Generated {len(df)} test documents")
    
    return df


if __name__ == '__main__':
    print("Generating NLP synthetic data...")
    
    # Create data directory
    import os
    os.makedirs('../data', exist_ok=True)
    
    # Generate training data
    train_df = generate_dataset(n_documents=2000, output_dir='../data')
    
    # Generate test data
    test_df = generate_test_set(n_documents=500, output_dir='../data')
    
    print(f"\nDataset summary:")
    print(f"  Total words: {train_df['word_count'].sum():,}")
    print(f"  Avg words/doc: {train_df['word_count'].mean():.1f}")
    print(f"  Date range: {train_df['created_date'].min()} to {train_df['created_date'].max()}")
    print("\nData generation complete.")
