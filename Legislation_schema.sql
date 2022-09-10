CREATE SCHEMA legislations
go

CREATE TABLE dbo.legislations(
	LegislationVersionId			int NOT NULL PRIMARY KEY,
	LegislationSourceId				int,
	Title							nvarchar(max),
	NativeTitle						nvarchar(max),
	IssuingBodyId					int,
	JurisdictionId					int

	FOREIGN KEY (IssuingBodyId) REFERENCES dbo.issuing_body (Id),
	FOREIGN KEY (JurisdictionId) REFERENCES dbo.jurisdiction (Id)
);

CREATE TABLE dbo.jurisdiction(
	Id					int PRIMARY KEY,
	Name				nvarchar(255),
	SourceId			UNIQUEIDENTIFIER

);

CREATE TABLE dbo.issuing_body(
	Id					int PRIMARY KEY,
	Name				nvarchar(255),
	SourceId			UNIQUEIDENTIFIER

);

CREATE TABLE dbo.part(
	PartVersionId					int PRIMARY KEY,
	LegislationVersionId			int,
	LegislationVersionOrdinal		int,
	PartSourceId					UNIQUEIDENTIFIER,
	PartVersionOrdinal				int,
	OrderNum						int,
	Content							nvarchar(max),
	NativeContent					nvarchar(max),
	ParentPartVersionId				int


	FOREIGN KEY (LegislationVersionId) REFERENCES dbo.legislations (LegislationVersionId)
);
