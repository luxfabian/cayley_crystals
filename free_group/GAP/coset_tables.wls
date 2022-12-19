#!/usr/bin/env wolframscript
(* ::Package:: *)

SetDirectory[NotebookDirectory[]];


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
(*Index of free group generators*)


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


FindCycle[g,{1}]


g = PureGraphF2[1];
HighlightGraph[g, FindCycle[ g,1 ] ]


MatRepresent[op_, sg_]:=(
	ctab = CosetTable[[sg]][[op]];
	
	dim = Length[ctab]; 
	
	mat = Table[ KroneckerDelta[i, ctab[[j]]],  {i,1,dim},{j,1,dim}];
	
	Return[mat];
);


Hamiltonian[sg_]:= Sum[ MatRepresent[i,sg],{i,1,4}]


Spectrum[sg_] :=Sort[Eigenvalues[Hamiltonian[sg]]]


IDS[\[Mu]_, spec_]:= N[ Count[  # < \[Mu] &/@ spec, True]/ Length[spec] ] 


pts = 1000;
\[Mu]s = Subdivide[-4,4,pts]//N;

ids[spec_]:= Transpose[{\[Mu]s, IDS[#,spec]&/@\[Mu]s}];


PlotSpectrum[sg_]:=ListLinePlot[
	ids[Spectrum[sg]] ,
	Frame-> True, 
	FrameLabel->{"\[Mu]","IDS"},
	(*PlotLabel-> "\!\(\*SubscriptBox[\(F\), \(2\)]\)/H = "<>Classification[[sg]],*)
	FrameStyle->16,
	LabelStyle->16
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





indices= DeleteCases[If[  Classification[[#]]!= "C"<>ToString[Length[CosetTable[[1]][[1]]]], #,None]&/@ Range[Length[CosetTable]] ,None]


(*plots = Analyze[#] &/@ Range[Length[CosetTable]] ;*)


indices= DeleteCases[If[  Classification[[#]]== "SL(2,3)", #,None]&/@ Range[Length[CosetTable]] ,None]


gfx=Analyze[#]&/@ indices ;


spec=Grid[ ArrayReshape[gfx,{4,4}] ];


Export["./output/SL(2,3).png",spec,ImageResolution-> 300];


GraphicsGrid[ ArrayReshape[gfx,{4,4}] ]


Length[indices]
