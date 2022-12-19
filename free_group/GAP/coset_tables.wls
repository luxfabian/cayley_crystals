#!/usr/bin/env wolframscript
(* ::Package:: *)

SetDirectory[If[$Notebooks, NotebookDirectory[], Directory[] ]];


data=Import["coset_tables.csv", "Text"];
CosetTable =ToExpression[ StringReplace[data,{ "[" -> "{", "]" -> "}"} ] ] ;


data = Import["quotients.csv","Text"];
Classification =ToExpression[ StringReplace[data,{ "[" -> "{", "]" -> "}"} ] ] ;


bc=BarChart[
	Sort[Counts[Classification]],  
	ChartLabels -> Automatic, 
	BarOrigin->Left,
	LabelStyle->12,
	ImageSize->300, 
	AspectRatio->2, 
	ColorFunction->"DarkBands", 
	GridLines->Automatic,
	AxesLabel->"Abs. frequency"
]
Export["./output/taxonomy.png", bc, ImageResolution -> 300]


(* ::Text:: *)
(*Index of free group generators (position of generators in basis set)*)


a = 1; 
b = 3;


colors[a]:= Red;
colors[b]:= Blue;
Represent[op_, sg_]:=(
	ctab = CosetTable[[sg]][[op]];
	graph = Table[Style[ DirectedEdge[i , ctab[[i]]],colors[op]], {i,1, Length[ctab]} ];
	Return[graph];
);


PureGraphF2[sg_]:=Represent[a,sg]~ Join ~ Represent[b,sg]
CayleyGraphF2[sg_]:= GraphPlot[PureGraphF2[sg] ,GraphLayout->"SpringElectricalEmbedding"]
CayleyGraphF23D[sg_]:= GraphPlot3D[ PureGraphF2[sg],GraphLayout->"SpringElectricalEmbedding"]


g = PureGraphF2[1];
HighlightGraph[g, FindCycle[ g,1 ] ]


(* ::Text:: *)
(*Matrix representation of the generators*)


MatRepresent[op_, sg_]:=(
	ctab = CosetTable[[sg]][[op]];
	
	dim = Length[ctab]; 
	
	mat = Table[ KroneckerDelta[i, ctab[[j]]],  {i,1,dim},{j,1,dim}];
	
	Return[mat];
);


(* ::Text:: *)
(*Definition of the Hamiltonian:*)


Hamiltonian[sg_]:= Sum[ MatRepresent[i,sg],{i,1,4}]


(* ::Text:: *)
(*and its spectrum:*)


Spectrum[sg_] :=Sort[Eigenvalues[Hamiltonian[sg]]]


(* ::Text:: *)
(*The integrated density of states can be computed from the spectrum as*)


IDS[\[Mu]_, spec_]:= N[ Count[  # < \[Mu] &/@ spec, True]/ Length[spec] ] 


(* ::Text:: *)
(*For the purposes of plotting the IDS, we define*)


pts = 1000;
\[Mu]s = Subdivide[-4,4,pts]//N;

ids[spec_]:= Transpose[{\[Mu]s, IDS[#,spec]&/@\[Mu]s}];


PlotSpectrum[sg_]:=ListLinePlot[
	ids[Spectrum[sg]] ,
	Frame-> True, 
	FrameLabel->{"x","F(x)"},
	PlotLabel-> "\!\(\*SubscriptBox[\(F\), \(2\)]\)/H = "<>Classification[[sg]],
	FrameStyle->20,
	LabelStyle->20
] 


Analyze[sg_]:=(
	gfx = GraphicsGrid[{{ CayleyGraphF2[sg]}, {PlotSpectrum[sg] }}];
	Export["./output/"<>StringPadLeft[ToString[sg],4,"0"]<>".png",gfx,ImageResolution-> 300];
	Return[gfx];
)

Analyze3D[sg_]:=(
	gfx = GraphicsGrid[{{ CayleyGraphF23D[sg]}, {PlotSpectrum[sg] }}];
	Export["./output/3D_"<>StringPadLeft[ToString[sg],4,"0"]<>".png",gfx,ImageResolution-> 300];
	(*Return[gfx];*)
)


gfx=Analyze[#]&/@ Range[Length[CosetTable]];


(* ::Text:: *)
(*Indices for which the factor group is isomorphic to SL(2,3)*)


SL23indices= DeleteCases[If[  Classification[[#]]== "SL(2,3)", #,None]&/@ Range[Length[CosetTable]] ,None]


(* ::Text:: *)
(*Adapt plotting for this case:*)


PlotSpectrum[sg_]:=ListLinePlot[
	ids[Spectrum[sg]] ,
	Frame-> True, 
	FrameLabel->{"x","F(x)"},
	FrameStyle->30,
	LabelStyle->30
] 

Analyze[sg_]:=(
	gfx = GraphicsGrid[{{ CayleyGraphF2[sg]}, {PlotSpectrum[sg] }}];
	Return[gfx];
)


gfx=Analyze[#]&/@ SL23indices;


spec=Grid[ ArrayReshape[gfx,{4,4}] ];


Export["./output/SL(2,3).png",spec,ImageResolution-> 300];
