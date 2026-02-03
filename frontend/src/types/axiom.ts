export interface SourceProof {
    documentName: string;
    originalAuthor: string;
    hash: string;
    pageRef?: number;
}

export interface MoltbookIdentity {
    agentId: string;
    karma: number;
    signature: string;
}

export interface Axiom {
    id: string;
    statement: string;
    confidenceScore: number; // 0.0 to 1.0
    tags: string[];
    source: SourceProof;
    validator: MoltbookIdentity;
    createdAt?: string;
}
