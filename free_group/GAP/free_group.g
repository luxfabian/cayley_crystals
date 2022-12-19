Display("~~~~ GAP 4.12.1 ~~~~");

LoadPackage("LINS");

# -----------------------------------------------------------

Display("Constructing the free group on two generators:");

G := FreeGroup("a","b");

Display(G);

# -----------------------------------------------------------

n := 24;
Display("Generating normal subgroups up to index:");
Display(n);

# all normal subgroups up to n
lins_search := LowIndexNormalSubgroupsSearchForIndex(G,n,infinity);

# only normal subgroups of index equal to n
lins_search_reduced := ComputedNormalSubgroups(lins_search);

# converting LINS data structure to standard GAP data structure
subgroups := List( lins_search_reduced, node -> Grp(node)  );

# calculate the quotient groups
quotients := List( subgroups, node -> StructureDescription(FactorGroup(G,node)));
quotient_relations := List( subgroups, node -> FactorGroup(G,node));

# calculate the group action on the quotient space
coset_tables := List( subgroups, node -> CosetTable(G,node));

relators := List( subgroups, node -> RelatorsOfFpGroup(SimplifiedFpGroup(Image(IsomorphismFpGroup(G / node)))) );

# Display(relators);

# # remove isomorphic duplicates
# isotypes  := DuplicateFreeList(quotients);

# Display("No. of subgroups of given index:");
# Display(Length(subgroups));
# Display(coset_tables[3]);

PrintTo("coset_tables.csv", coset_tables);
PrintTo("quotients.csv", quotients);
PrintTo("relations.csv", relators);
