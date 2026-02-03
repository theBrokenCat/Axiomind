import React, { useState } from 'react';
import { Search, Loader2 } from 'lucide-react';
import { cn } from '../lib/utils';

interface SearchBarProps {
    onSearch: (query: string) => void;
    isLoading?: boolean;
    className?: string;
}

export const SearchBar: React.FC<SearchBarProps> = ({ onSearch, isLoading, className }) => {
    const [query, setQuery] = useState('');
    const [isFocused, setIsFocused] = useState(false);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (query.trim()) {
            onSearch(query);
        }
    };

    return (
        <form onSubmit={handleSubmit} className={cn("relative w-full max-w-2xl group", className)}>
            {/* Glow Effect Background */}
            <div
                className={cn(
                    "absolute -inset-0.5 bg-gradient-to-r from-axiom to-blue-600 rounded-full blur opacity-20 transition duration-1000 group-hover:opacity-50",
                    isFocused && "opacity-75 blur-md"
                )}
            ></div>

            <div className="relative flex items-center bg-black rounded-full border border-white/10 p-2">
                <Search className={cn("ml-4 w-5 h-5 text-gray-400 transition-colors", isFocused && "text-axiom")} />

                <input
                    type="text"
                    value={query}
                    onChange={(e) => setQuery(e.target.value)}
                    onFocus={() => setIsFocused(true)}
                    onBlur={() => setIsFocused(false)}
                    placeholder="Ask the Axiom..."
                    className="w-full bg-transparent border-none focus:ring-0 text-white placeholder-gray-500 px-4 py-2 text-lg outline-none"
                    disabled={isLoading}
                />

                <button
                    type="submit"
                    disabled={isLoading || !query.trim()}
                    className={cn(
                        "p-2 rounded-full bg-white/5 hover:bg-white/10 text-white transition-all disabled:opacity-50 disabled:cursor-not-allowed",
                        query.trim() && !isLoading && "bg-axiom/20 text-axiom hover:bg-axiom/30 shadow-[0_0_15px_rgba(0,240,255,0.3)]"
                    )}
                >
                    {isLoading ? <Loader2 className="w-5 h-5 animate-spin" /> : <span className="px-2 text-sm font-semibold">SEEK</span>}
                </button>
            </div>
        </form>
    );
};
