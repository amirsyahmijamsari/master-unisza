"use client"

import { useState } from 'react'
import { ChevronUp, ChevronDown } from 'lucide-react'

interface Column<T> {
  key: keyof T | string;
  header: string;
  render?: (item: T) => React.ReactNode;
  sortable?: boolean;
}

interface DataTableProps<T> {
  data: T[];
  columns: Column<T>[];
  pageSize?: number;
}

export function DataTable<T extends object>({ 
  data, 
  columns, 
  pageSize = 10 
}: DataTableProps<T>) {
  const [currentPage, setCurrentPage] = useState(0)
  const [sortColumn, setSortColumn] = useState<string | null>(null)
  const [sortDirection, setSortDirection] = useState<'asc' | 'desc'>('asc')

  const handleSort = (key: string) => {
    if (sortColumn === key) {
      setSortDirection(prev => prev === 'asc' ? 'desc' : 'asc')
    } else {
      setSortColumn(key)
      setSortDirection('asc')
    }
  }

  const sortedData = [...data].sort((a, b) => {
    if (!sortColumn) return 0
    const aVal = (a as Record<string, unknown>)[sortColumn]
    const bVal = (b as Record<string, unknown>)[sortColumn]
    if (aVal === null || aVal === undefined) return 1
    if (bVal === null || bVal === undefined) return -1
    if (typeof aVal === 'number' && typeof bVal === 'number') {
      return sortDirection === 'asc' ? aVal - bVal : bVal - aVal
    }
    return sortDirection === 'asc' 
      ? String(aVal).localeCompare(String(bVal))
      : String(bVal).localeCompare(String(aVal))
  })

  const totalPages = Math.ceil(sortedData.length / pageSize)
  const paginatedData = sortedData.slice(currentPage * pageSize, (currentPage + 1) * pageSize)

  return (
    <div className="overflow-hidden rounded-xl border border-slate-200 shadow-sm">
      <div className="overflow-x-auto">
        <table className="w-full">
          <thead className="bg-slate-50">
            <tr>
              {columns.map(col => (
                <th 
                  key={String(col.key)}
                  className={`px-4 py-3 text-left text-xs font-semibold text-slate-600 uppercase tracking-wider ${col.sortable ? 'cursor-pointer hover:bg-slate-100' : ''}`}
                  onClick={() => col.sortable && handleSort(String(col.key))}
                >
                  <div className="flex items-center gap-1">
                    {col.header}
                    {col.sortable && sortColumn === String(col.key) && (
                      sortDirection === 'asc' ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />
                    )}
                  </div>
                </th>
              ))}
            </tr>
          </thead>
          <tbody className="divide-y divide-slate-100">
            {paginatedData.map((item, idx) => (
              <tr key={idx} className="bg-white hover:bg-slate-50 transition-colors">
                {columns.map(col => (
                  <td key={String(col.key)} className="px-4 py-3 text-sm text-slate-700">
                    {col.render ? col.render(item) : String((item as Record<string, unknown>)[col.key as string] ?? '-')}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      
      {totalPages > 1 && (
        <div className="flex items-center justify-between px-4 py-3 bg-slate-50 border-t border-slate-200">
          <span className="text-sm text-slate-500">
            Showing {currentPage * pageSize + 1} to {Math.min((currentPage + 1) * pageSize, data.length)} of {data.length}
          </span>
          <div className="flex gap-2">
            <button
              onClick={() => setCurrentPage(p => Math.max(0, p - 1))}
              disabled={currentPage === 0}
              className="px-3 py-1.5 text-sm rounded-lg bg-white border border-slate-300 text-slate-700 hover:bg-slate-50 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
            >
              Previous
            </button>
            <button
              onClick={() => setCurrentPage(p => Math.min(totalPages - 1, p + 1))}
              disabled={currentPage >= totalPages - 1}
              className="px-3 py-1.5 text-sm rounded-lg bg-white border border-slate-300 text-slate-700 hover:bg-slate-50 disabled:opacity-50 disabled:cursor-not-allowed shadow-sm"
            >
              Next
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
