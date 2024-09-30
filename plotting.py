sns.catplot(
    data=df1, x="Concentration (uM)", y="Median Intensity Value", row="Binding motif",col="Linker type",
    kind="bar", order = ['100uM','10uM','1uM','100nM','10nM','0nM'], sharex=False, height=8, aspect=0.9
)
#plt.xticks(rotation=45)
#plt.xlabel('Concentration (uM)')
#plt.title('Nearly 100% Volume Wash + Longer Incubation at 37C')
plt.savefig('results_Francis_20240809', dpi=300, bbox_inches='tight')