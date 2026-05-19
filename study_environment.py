df['study_environment'] = df['study_environment'].str.strip()

study_environment_map = {
    "Private space (i.e. bedroom, home office)": "Private Space",
    "Open learning space (i.e. university library)": "Open Space",
    "Collaborative space (i.e. group study room)": "Collab Space",
    "Cafes": "Café",
    
    "Dormitory": "Private Space",
    "Any quiet space": "Private Space",
    "Flexible": "Flexible/Multiple",
    "Flexible, could be private place or open learning space": "Flexible/Multiple",
    "All above": "Flexible/Multiple",
    "all places above, and all places possible like pantry rooms, JA102, etc": "Flexible/Multiple"
}

df['study_environment'] = df['study_environment'].map(study_environment_map)
print(df['study_environment'].value_counts())
# Plot study location vs focus
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='study_environment', hue='focus_frequency')
plt.title('Focus frequency vs. Study environment')
plt.show()
# plot study environment vs study hours
plt.figure(figsize=(12, 6))
sns.boxplot(data=df, x='study_environment', y='self_study_hours')
plt.title('Study environment vs. Study hours')
plt.show()