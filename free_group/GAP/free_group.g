Display("~~~~ GAP 4.12.1 ~~~~");

LoadPackage("LINS");

# -----------------------------------------------------------

Display("Constructing the free group on two generators:");

G := FreeGroup("a","b");

Display(G);

# -----------------------------------------------------------
n := 32;
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

PrintTo("./output/coset_tables.csv", coset_tables);
Display("Coset tables have been stored to ./output/coset_tables.csv");
PrintTo("./output/quotients.csv", quotients);
Display("Classification of factor groups has been stored to ./output/quotients.csv");

