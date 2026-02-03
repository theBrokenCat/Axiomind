import React from 'react';
import type { Axiom } from '../types/axiom';
import { ShieldCheck, FileText, Hash, User, ExternalLink } from 'lucide-react';
import { cn } from '../lib/utils';
import { motion } from 'framer-motion';

interface AxiomCardProps {
    axiom: Axiom;
    className?: string;
}

export const AxiomCard: React.FC<AxiomCardProps> = ({ axiom, className }) => {
    const confidencePercent = Math.round(axiom.confidenceScore * 100);

    // Dynamic color based on confidence
    const confidenceColor =
        confidencePercent >= 90 ? "text-axiom" :
            confidencePercent >= 70 ? "text-emerald-400" :
                "text-amber-500";

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            className={cn(
                "relative w-full max-w-2xl overflow-hidden rounded-xl border border-white/10 bg-surface backdrop-blur-md transition-all hover:bg-surface-hover hover:border-axiom/50 hover:shadow-[0_0_30px_rgba(0,240,255,0.15)]",
                className
            )}
        >
            {/* Header: Statement */}
            <div className="p-6 md:p-8">
                <div className="flex justify-between items-start gap-4">
                    <h2 className="text-2xl font-light text-text-primary leading-tight tracking-wide">
                        {axiom.statement}
                    </h2>
                    <div className={`flex flex-col items-center justify-center p-3 rounded-full bg-black/20 border border-white/5 ${confidenceColor}`}>
                        <span className="text-xl font-bold">{confidencePercent}%</span>
                        <span className="text-[10px] uppercase tracking-wider opacity-70">Truth</span>
                    </div>
                </div>

                {/* Tags */}
                <div className="flex flex-wrap gap-2 mt-4">
                    {axiom.tags.map((tag) => (
                        <span key={tag} className="px-3 py-1 text-xs text-axiom bg-axiom/10 rounded-full border border-axiom/20">
                            #{tag}
                        </span>
                    ))}
                </div>
            </div>

            {/* Footer: Metadata Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-px bg-white/5 border-t border-white/10">

                {/* Source Section */}
                <div className="p-6 space-y-3 bg-black/20 backdrop-blur-sm">
                    <div className="flex items-center gap-2 text-sm text-text-muted mb-2">
                        <FileText size={16} />
                        <span className="uppercase tracking-widest text-xs">Source Origin</span>
                    </div>
                    <div className="space-y-1">
                        <div className="text-text-secondary text-sm font-medium flex items-center gap-2">
                            {axiom.source.documentName}
                            {axiom.source.pageRef && <span className="text-xs text-text-muted">(Pg. {axiom.source.pageRef})</span>}
                        </div>
                        <div className="text-xs text-text-muted flex items-center gap-2 truncate" title={axiom.source.hash}>
                            <Hash size={12} />
                            {axiom.source.hash.substring(0, 16)}...
                        </div>
                        <div className="text-xs text-source flex items-center gap-2">
                            <User size={12} />
                            {axiom.source.originalAuthor}
                        </div>
                    </div>
                </div>

                {/* Validator Section */}
                <div className="p-6 space-y-3 bg-black/20 backdrop-blur-sm">
                    <div className="flex items-center gap-2 text-sm text-text-muted mb-2">
                        <ShieldCheck size={16} className="text-moltbook" />
                        <span className="uppercase tracking-widest text-xs">Verified By</span>
                    </div>

                    <div className="space-y-1">
                        <div className="text-text-secondary text-sm font-medium flex items-center gap-2">
                            ID: {axiom.validator.agentId}
                            <ExternalLink size={12} className="opacity-50 hover:opacity-100 cursor-pointer" />
                        </div>
                        <div className="text-xs text-moltbook flex items-center gap-2">
                            Running Karma: {axiom.validator.karma.toLocaleString()}
                        </div>
                        <div className="text-[10px] text-text-muted font-mono mt-1 opacity-50 truncate" title={axiom.validator.signature}>
                            Sig: {axiom.validator.signature.substring(0, 20)}...
                        </div>
                    </div>
                </div>

            </div>
        </motion.div>
    );
};
