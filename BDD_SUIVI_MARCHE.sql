create table [Marche]
(
    [Num_Contrat]       varchar(25)        not null
        constraint PK_Cle_Num_Contrat
            primary key,
    [Num_Avenant]       int       default 0 ,
    [Code_Site]         varchar(10)         not null,
    [NT]                varchar(20)         not null,
    [Libelle]           varchar(max) 				,
    [Ods_Depart]        date                not null,
    [Delais]            int,
    [Revisable]         bit       default 0,
    [Actualisable]      bit       default 0,
	[Delai_Paiement_F]  int       default 0,
    [Rabais]            float     default 0,
    [Tva]               float     default 0,
    [Rg]                float     default 0,
    [Date_Signature]    date                not null,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP,
)
go

create index [INDEX_Marche_Code_Site]
    on [Marche] ([Code_Site])
go

create index [INDEX_Marche_NT]
    on [Marche] ([NT])
go

create index [INDEX_Marche_Num_Avenant]
    on [Marche] ([Num_Avenant])
go

create index [INDEX_Marche_Est_Bloquer]
    on [Marche] ([Est_Bloquer])
go


create index [INDEX_Marche_User_ID]
    on [Marche] ([User_ID])
go

create index [INDEX_Marche_Date_Modification]
    on [Marche] ([Date_Modification])
go


/******************************************************************/

create table [Marche_Avenant]
(
    [Num_Contrat]       varchar(25)        not null,
    [Num_Avenant]       int       default 0 ,
    [Code_Site]         varchar(10)         not null,
    [NT]                varchar(20)         not null,
    [Libelle]           varchar(max)        ,
    [Ods_Depart]        date                not null,
    [Delais]            int,
    [Revisable]         bit       default 0,
    [Actualisable]      bit       default 0,
	[Delai_Paiement_F]  int       default 0,
    [Rabais]            float     default 0,
    [Tva]               float     default 0,
    [Rg]                float     default 0,
    [Date_Signature]    date                not null,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP,

	CONSTRAINT PK_Cle_Num_Contrat_Num_Avenant PRIMARY KEY  ([Num_Contrat],[Num_Avenant])

)
go

create index [INDEX_Marche_Avenant_Code_Site]
    on [Marche_Avenant] ([Code_site])
go

create index [INDEX_Marche_Avenant_NT]
    on [Marche_Avenant] ([NT])
go

create index [INDEX_Marche_Avenant_Num_Avenant]
    on [Marche_Avenant] ([Num_Avenant])
go

create index [INDEX_Marche_Avenant_Num_Contrat]
    on [Marche_Avenant] ([Num_Contrat])
go


create index [INDEX_Marche_Avenant_Est_Bloquer]
    on [Marche_Avenant] ([Est_Bloquer])
go


create index [INDEX_Marche_Avenant_User_ID]
    on [Marche_Avenant] ([User_ID])
go

create index [INDEX_Marche_Avenant_Date_Modification]
    on [Marche_Avenant] ([Date_Modification])
go



/******************************************************************/
create table [Mode_Paiement]
(
    [Id_Mode]          varchar(3) /* v : virement  ou c :chéque */
        constraint PK_Cle_Id_Mode
            primary key,

    [libelle]           varchar(50) not null,
    [Est_Bloquer] BIT DEFAULT 0,
     [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
)
go

create index [INDEX_Mode_Paiement_Est_Bloquer]
    on [Mode_Paiement] ([Est_Bloquer])
go


create index [INDEX_Mode_Paiement_User_ID]
    on [Mode_Paiement] ([User_ID])
go

create index [INDEX_Mode_Paiement_Date_Modification]
    on [Mode_Paiement] ([Date_Modification])
go

/******************************************************************/

create table [Type_Avance]
(
    [Id_Type_Avance]    varchar(3) /* A : appro , F: forf  E: Except (autres)*/
        constraint PK__Cle_Id_Type_Avance
            primary key,
    [Libelle]           varchar(50) not null,
    [Taux]              float        default 0 ,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
)
go

create index [INDEX_Type_Avance_Est_Bloquer]
    on [Type_Avance] ([Est_Bloquer])
go


create index [INDEX_Type_Avance_User_ID]
    on [Type_Avance] ([User_ID])
go

create index [INDEX_Type_Avance_Date_Modification]
    on [Type_Avance] ([Date_Modification])
go




/******************************************************************/

create table [Type_Caution]
(
    [Id_Type_Caution]   varchar(5) /* CS : Caution Soumission , CBE : Caution bonne exec, CAF : Caution Avance Forf , CAA: Caution Avance Appro, CAE :Caution Avance Except ... */
        constraint PK__Cle_Id_Type_Caution
            primary key,
    [libelle]           varchar(50) not null,
    [Taux_Exact]        float null,
    [Taux_Min]          float null,
    [Taux_Max]          float null,
    [Type_Avance]       varchar(3),
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
)
go
create index [INDEX_Type_Caution_Est_Bloquer]
    on [Type_Caution] ([Est_Bloquer])
go


create index [INDEX_Type_Caution_User_ID]
    on [Type_Caution] ([User_ID])
go

create index [INDEX_Type_Caution_Date_Modification]
    on [Type_Caution] ([Date_Modification])
go



/******************************************************************/

create table [Avances]
(
    [Id_Avance]         varchar(30) /*AA:Avance Appro    AF:Avance Frof  AE :Avance Excep + numero_avance   AA0 AA1 AA2...  */
        constraint PK_Cle_Id_avance
            primary key,
    [Num_Avance]        int       not null,
    [Taux_Avance]       float     default 0 ,
    [Montant]           float     not null,
    [Taux_Debut_Remb]             float     default 0  ,
    [Taux_Fin_Remb]               float     default 80 ,
    [Date_Avance]              date                 not null,
    [Remboursee]        bit       default 0 ,
    [Num_Marche ]     varchar(25)         not null,
    [Type_Avance]       varchar(3)        not null,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
)
go

create index [INDEX_Avances_Type_Avance]
    on [Avances] ([Type_Avance])
go
create index [INDEX_Avances_Remboursee]
    on [Avances] ([Remboursee])
go

create index [INDEX_Avances_Est_Bloquer]
    on [Avances] ([Est_Bloquer])
go


create index [INDEX_Avances_User_ID]
    on [Avances] ([User_ID])
go

create index [INDEX_Avances_Date_Modification]
    on [Avances] ([Date_Modification])
go


/******************************************************************/

create table [Cautions]
(
    [Id_Caution]        varchar(30) /*AA:Avance Appro    AF:Avance Frof  AE :Avance Excep + numero_avance   AA0 AA1 AA2...  */
        constraint PK_Cle_Id_Caution
            primary key,
    [Date_Soumission]   date        not null,
    [Montant]           float       not null,
    [Est_Recupere]      bit         default 0,
    [Agence]            varchar(15) not null,
    [Avance]            varchar(30) null,
    [Num_Marche]        varchar(25),
    [Type_Caution]      varchar(5)         not null,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
)
go

create index [INDEX_Cautions_Num_Marche_id]
    on [Cautions] ([Num_Marche])
go

create index [INDEX_Cautions_Type_Caution]
    on [Cautions] ([Type_Caution])
go

create index [INDEX_Cautions_Avance]
    on [Cautions] ([Avance])
go
create index [INDEX_Cautions_Est_Recupere]
    on [Cautions] ([Est_Recupere])
go
create index [INDEX_Cautions_Est_Bloquer]
    on [Cautions] ([Est_Bloquer])
go


create index [INDEX_Cautions_User_ID]
    on [Cautions] ([User_ID])
go

create index [INDEX_Cautions_Date_Modification]
    on [Cautions] ([Date_Modification])
go



/******************************************************************/



create table [Tab_NT_Taches_Avenant]
(
    [Code_Site]                varchar(10) not null,
    [NT]                     varchar(20) not null,
    [Code_Tache]               varchar(30) not null,
    [Num_Avenant]              int          default 0,
    [Est_Tache_Composite]      bit          default 0,
    [Est_Tache_Complementaire] bit          default 0,
    [Libelle_Tache]            varchar(max) default NULL,
    [Code_Unite_Mesure]        varchar(4)   default NULL,
    [Quantite]                 real         default 0,
    [Prix_Unitaire]            money        default 0,
    [Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
	CONSTRAINT PK_Cle_Code_Site_NT_Code_Tache_Num_Avenant PRIMARY KEY  ([Code_site], [NT], [Code_Tache],[Num_Avenant])

)
go

create index [INDEX_Tab_NT_Taches_Avenant_Code_site]
    on [Tab_NT_Taches_Avenant] ([Code_site])
go

create index [INDEX_Tab_NT_Taches_Avenant_NT]
    on [Tab_NT_Taches_Avenant] ([NT])
go

create index [Tab_NT_Taches_Avenant_Code_Tache]
    on [Tab_NT_Taches_Avenant] ([Code_Tache])
go

create index [INDEX_Tab_NT_Taches_Avenant_Num_Avenant]
    on [Tab_NT_Taches_Avenant] ([Num_Avenant])
go
create index [INDEX_Tab_NT_Taches_Avenant_Est_Bloquer]
    on [Tab_NT_Taches_Avenant] ([Est_Bloquer])
go


create index [INDEX_Tab_NT_Taches_Avenant_User_ID]
    on [Tab_NT_Taches_Avenant] ([User_ID])
go

create index [INDEX_Tab_NT_Taches_Avenant_Date_Modification]
    on [Tab_NT_Taches_Avenant] ([Date_Modification])
go





/******************************************************************/


create table [Factures]
(
    [Num_Facture]       varchar(30) not null
        constraint PK_Cle_Num_Facture
            primary key,
    [Num_Situation]     int          not null,
    [Date_Debut]        date         not null, /*du*/
    [Date_Fin]         date         not null, /*au*/
    [Date_Facture]      date         not null,
    [Montant_Mois]      float     default 0,
    [Montant_RB]        float     default 0,
    [Montant_RG]        float     default 0,
    [Paye]              bit       default 0,
    [Num_Marche]        varchar(25) not null,
	[Est_Bloquer] BIT DEFAULT 0,
     [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP,

)
go

create index [INDEX_Factures_Num_Facture]
    on [Factures] ([Num_facture])
go

create index [INDEX_Factures_Num_Situation]
    on [Factures] ([Num_Situation])
go

create index [INDEX_Factures_Paye]
    on [Factures] ([Paye])
go


create index [INDEX_Factures_Est_Bloquer]
    on [Factures] ([Est_Bloquer])
go


create index [INDEX_Factures_User_ID]
    on [Factures] ([User_ID])
go

create index [INDEX_Factures_Date_Modification]
    on [Factures] ([Date_Modification])
go





/******************************************************************/



create table [Attachements]
(
    [Id_Attachement]    varchar(30)
        constraint Attachements_pk
            primary key,
    [Num_Marche]        varchar(25),
    [Code_Site]         varchar(10) not null,
    [NT]                varchar(20) not null,
    [Code_Tache]        varchar(30) not null,
    [Quantite]               float     default 0,
    [Prix_Unitaire]            float     default 0,
    [Montant]           float     default 0,
    [Mmaa]              date        not null,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP,

)
go

create index [INDEX_Attachements_Code_Site]
    on [Attachements] ([Code_Site])
go

create index [INDEX_Attachements_NT]
    on [Attachements] ([NT])
go

create index [INDEX_Attachements_Code_Tache]
    on [Attachements] ([Code_Tache])
go

create index [INDEX_Attachements_Num_Marche]
    on [Attachements] ([Num_Marche])
go

create index [INDEX_Attachements_Mmaa]
    on [Attachements] ([Mmaa])
go


create index [INDEX_Attachements_Est_Bloquer]
    on [Attachements] ([Est_Bloquer])
go


create index [INDEX_Attachements_User_ID]
    on [Attachements] ([User_ID])
go

create index [INDEX_Attachements_Date_Modification]
    on [Attachements] ([Date_Modification])
go


/**********************************************/


create table [Detail_Facture]
(
    [Id_Df]                int identity
        constraint PK_Cle_Id_Df
            primary key,

	[Num_Facture]       varchar(30) not null,
    [Detail]            varchar(30)  not null,


	[Est_Bloquer] BIT DEFAULT 0,
	[User_ID]           varchar(15) ,
    [Date_Modification] datetime2  DEFAULT CURRENT_TIMESTAMP   ,

)
go

create index [INDEX_Detail_Facture_facture_id]
    on [Detail_Facture] ([Num_Facture])
go
create index [INDEX_Detail_Facture_Detail]
    on [Detail_Facture] ([Detail])
go

create index [INDEX_Detail_Facture_Est_Bloquer]
    on [Detail_Facture] ([Est_Bloquer])
go


create index [INDEX_Detail_Facture_User_ID]
    on [Detail_Facture] ([User_ID])
go

create index [INDEX_Detail_Facture_Date_Modification]
    on [Detail_Facture] ([Date_Modification])
go



/************************************************/


create table [Remboursement]
(
    [Id_Remb]                int identity
        constraint PK_Cle_Id_Remb
            primary key,
    [Montant]           float     default 0 not null,
    [Avance]            varchar(30),
    [Num_Facture]       varchar(30),
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP
)
go

create index [INDEX_Rembourcement_Num_Facture]
    on [Remboursement] ([Num_Facture])
go

create index [INDEX_Rembourcement_Avance_id]
    on [Remboursement] ([Avance])
go

create index [INDEX_Remboursement_Est_Bloquer]
    on [Remboursement] ([Est_Bloquer])
go


create index [INDEX_Remboursement_User_ID]
    on [Remboursement] ([User_ID])
go

create index [INDEX_Remboursement_Date_Modification]
    on [Remboursement] ([Date_Modification])
go


/***************************************************************************/

create table [Encaissements]
(
    [Id_Enc]                bigint identity
        constraint PK_Cle_Id_Enc
            primary key,
    [Date_Encaissement] date          not null,
    [Montant_Encaisse]  float         not null,
    [Numero_Piece]      varchar(30) not null,
    [Agence]         varchar(15),
    [Facture]        varchar(30) not null,
    [Mode_Paiement]  varchar(3) ,
	[Est_Bloquer] BIT DEFAULT 0,
    [User_ID]           varchar(15),
    [Date_Modification] DATETIME2 (7)DEFAULT CURRENT_TIMESTAMP

)
go


create index [INDEX_Encaissements_Facture]
    on [Encaissements] ([Facture])
go

create index [INDEX_Encaissements_Mode_Paiement]
    on [Encaissements] ([Mode_Paiement])
go
create index [INDEX_Encaissements_Date_Encaissement]
    on [Encaissements] ([Date_Encaissement])
go

create index [INDEX_Encaissements_Est_Bloquer]
    on [Remboursement] ([Est_Bloquer])
go


create index [INDEX_Encaissements_User_ID]
    on [Remboursement] ([User_ID])
go

create index [INDEX_Encaissements_Date_Modification]
    on [Remboursement] ([Date_Modification])
go


/***************************************************************************/
/*Marche*/
ALTER TABLE [Marche] ADD CONSTRAINT FK_Cle_Code_Site_NT_Marche FOREIGN KEY  ([Code_Site],[NT]) REFERENCES [Tab_NT] ([Code_site],[NT]);

/*Marche_Avenant*/
ALTER TABLE [Marche_Avenant] ADD CONSTRAINT FK_Cle_Code_Site_NT_Marche_Avenant FOREIGN KEY  ([Code_Site],[NT]) REFERENCES [Tab_NT] ([Code_site],[NT]);

/*Type_Caution*/
ALTER TABLE [Type_Caution] ADD CONSTRAINT FK_Cle_Type_Avance_Type_Caution FOREIGN KEY  ([Type_Avance]) REFERENCES [Type_Avance] ([Id_Type_Avance]);


/*Avances*/
ALTER TABLE [Avances] ADD CONSTRAINT FK_Cle_Num_Marche_Avances FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );
ALTER TABLE [Avances] ADD CONSTRAINT FK_Cle_Type_Avance_Avances FOREIGN KEY  ([Type_Avance]) REFERENCES [Type_Avance] ([Id_Type_Avance]);



/*Cautions*/
ALTER TABLE [Cautions] ADD CONSTRAINT FK_Cle_Num_Marche_Cautions FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );
ALTER TABLE [Cautions] ADD CONSTRAINT FK_Cle_Agence_Cautions FOREIGN KEY  ([Agence]) REFERENCES [Tab_Agence] ([Code_Agence] );
ALTER TABLE [Cautions] ADD CONSTRAINT FK_Cle_Type_Caution_Cautions FOREIGN KEY  ([Type_Caution]) REFERENCES [Type_Caution] ([Id_Type_Caution]);
ALTER TABLE [Cautions] ADD CONSTRAINT FK_Cle_Avance_Cautions FOREIGN KEY  ([Avance]) REFERENCES [Avances] ([Id_Avance]);



/*Tab_NT_Taches_Avenant*/
ALTER TABLE [Tab_NT_Taches_Avenant] ADD CONSTRAINT FK_Cle_Code_Site_NT_Tab_NT_Taches_Avenant FOREIGN KEY  ([Code_Site],[NT]) REFERENCES [Tab_NT] ([Code_site],[NT]);
ALTER TABLE [Tab_NT_Taches_Avenant] ADD CONSTRAINT FK_Cle_Code_Unite_Mesure_Tab_NT_Taches_Avenant FOREIGN KEY  ([Code_Unite_Mesure]) REFERENCES [Tab_Unite_de_Mesure] ([Code_Unite_Mesure]);


/*Factures*/
ALTER TABLE [Factures] ADD CONSTRAINT FK_Cle_Num_Marche_Factures FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );


/*Attachements*/
ALTER TABLE [Attachements] ADD CONSTRAINT FK_Cle_Code_Site_NT_Code_Tache_Table_Attachements FOREIGN KEY  ([Code_Site],[NT],[Code_Tache]) REFERENCES [Tab_NT_Taches] ([Code_Site],[NT],[Code_Tache]);
ALTER TABLE [Attachements] ADD CONSTRAINT FK_Cle_Num_Marche_Attachements FOREIGN KEY  ([Num_Marche]) REFERENCES [Marche] ([Num_Contrat] );


/*Detail_Facture*/
ALTER TABLE [Detail_Facture] ADD CONSTRAINT FK_Cle_Num_Facture_Detail_facture FOREIGN KEY  ([Num_Facture]) REFERENCES [Factures] ([Num_facture] );
ALTER TABLE [Detail_Facture] ADD CONSTRAINT FK_Cle_Detail_Detail_facture FOREIGN KEY  ([Detail]) REFERENCES [Attachements] ([Id_Attachement] );



/*Remboursement*/
ALTER TABLE [Remboursement] ADD CONSTRAINT FK_Cle_Num_Facture_Remboursement FOREIGN KEY  ([Num_Facture]) REFERENCES [Factures] ([Num_facture] );
ALTER TABLE [Remboursement] ADD CONSTRAINT FK_Cle_Avance_Remboursement FOREIGN KEY  ([Avance]) REFERENCES [Avances] ([Id_Avance]);

/*Encaissement*/

ALTER TABLE [Encaissements] ADD CONSTRAINT FK_Cle_Facture_Encaissements FOREIGN KEY  ([Facture]) REFERENCES [Factures] ([Num_Facture]);
ALTER TABLE [Encaissements] ADD CONSTRAINT FK_Cle_Agence_Encaissements FOREIGN KEY  ([Agence]) REFERENCES [Tab_Agence] ([Code_Agence] );
ALTER TABLE [Encaissements] ADD CONSTRAINT FK_Cle_Mode_Paiement_Encaissements FOREIGN KEY  ([Mode_Paiement]) REFERENCES [Mode_Paiement] ([Id_Mode] );



