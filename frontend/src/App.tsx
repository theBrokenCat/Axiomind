import { useState } from 'react';
import { AxiomCard } from './components/AxiomCard';
import { SearchBar } from './components/SearchBar';
import type { Axiom } from './types/axiom';
import { Sparkles } from 'lucide-react';

// Mock Data
const MOCK_AXIOMS: Record<string, Axiom> = {
  "default": {
    id: "ax_9921",
    statement: "The integration of AI into decentralized governance requires verifiable reputation systems to prevent Sybil attacks.",
    confidenceScore: 0.94,
    tags: ["governance", "security", "ai-safety"],
    source: {
      documentName: "Protocol_Manifesto_v3.pdf",
      originalAuthor: "S. Nakamoto II",
      hash: "0x8f2...9a1",
      pageRef: 42
    },
    validator: {
      agentId: "mbot_alpha_1",
      karma: 8500,
      signature: "sig_rsa_4096_valid_check"
    },
    createdAt: new Date().toISOString()
  },
  "low": {
    id: "ax_002",
    statement: "Water memory implies emotional transference in molecular structures.",
    confidenceScore: 0.12,
    tags: ["pseudoscience", "fringe", "water"],
    source: {
      documentName: "Blog_Post_2021.txt",
      originalAuthor: "Anon_Blogger",
      hash: "0x1a2...bb4",
    },
    validator: {
      agentId: "mbot_beta_2",
      karma: 120,
      signature: "sig_invalid_format"
    }
  }
};

function App() {
  const [axiom, setAxiom] = useState<Axiom | null>(null);
  const [loading, setLoading] = useState(false);
  const [hasSearched, setHasSearched] = useState(false);

  const handleSearch = (query: string) => {
    setLoading(true);
    // Simulate API call
    setTimeout(() => {
      // Simple mock logic: if query contains "water" return low confidence, else high
      const result = query.toLowerCase().includes("water") ? MOCK_AXIOMS["low"] : MOCK_AXIOMS["default"];
      setAxiom(result);
      setLoading(false);
      setHasSearched(true);
    }, 1500);
  };

  return (
    <div className="min-h-screen w-full flex flex-col items-center justify-center p-4 relative">
      {/* Background Decor - Optional Orbitals */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-1/4 left-1/4 w-96 h-96 bg-axiom/10 rounded-full blur-[100px] animate-pulse-slow"></div>
        <div className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-purple-500/10 rounded-full blur-[100px] animate-pulse-slow delay-1000"></div>
      </div>

      <div className="z-10 w-full max-w-4xl flex flex-col items-center gap-12">

        {/* Header / Logo Area */}
        <div className={`transition-all duration-700 flex flex-col items-center ${hasSearched ? 'scale-75 -translate-y-8' : 'scale-100'}`}>
          <div className="flex items-center gap-3 mb-2">
            <Sparkles className="text-axiom w-8 h-8" />
            <h1 className="text-4xl font-extralight tracking-[0.2em] text-white">
              AXIO<span className="font-bold text-axiom">MIND</span>
            </h1>
          </div>
          <p className="text-text-muted text-sm tracking-widest uppercase opacity-70">
            Truth Resonance Chamber
          </p>
        </div>

        {/* Search */}
        <div className="w-full flex justify-center">
          <SearchBar onSearch={handleSearch} isLoading={loading} />
        </div>

        {/* Results Area */}
        <div className="w-full flex justify-center min-h-[300px]">
          {loading && (
            <div className="text-axiom animate-pulse flex flex-col items-center gap-4 mt-8">
              <div className="w-16 h-16 border-4 border-axiom/30 border-t-axiom rounded-full animate-spin"></div>
              <span className="tracking-widest text-xs uppercase">Synthesizing Truth...</span>
            </div>
          )}

          {!loading && axiom && (
            <AxiomCard axiom={axiom} />
          )}
        </div>

      </div>

      {/* Footer */}
      <div className="absolute bottom-4 text-xs text-white/20 font-mono">
        v0.1.0-alpha // SYSTEM: ONLINE
      </div>
    </div>
  );
}

export default App;
