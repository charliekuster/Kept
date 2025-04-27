import { useState } from "react";
import { Search, Calendar, MapPin, ChevronDown } from "lucide-react";
import "./Sidebar.css";

const FilterItem = ({ label, icon: Icon, hasSearch = false }) => {
  const [open, setOpen] = useState(false);
  const [searchValue, setSearchValue] = useState("");

  return (
    <div className="filter-item">
      <div className="filter-header" onClick={() => setOpen(!open)}>
        <div className="filter-label">
          <Icon className="filter-icon" size={18} />
          <span>{label}</span>
        </div>
        <ChevronDown
          className={`chevron-icon ${open ? "rotate-180" : ""}`}
          size={18}
        />
      </div>
      {open && (
        <div className="filter-content">
          {hasSearch && (
            <input
              type="text"
              className="filter-input"
              placeholder={`Search ${label}`}
              value={searchValue}
              onChange={(e) => setSearchValue(e.target.value)}
            />
          )}
          {/* Aqui poderiam vir opções filtradas */}
        </div>
      )}
    </div>
  );
};

const FilterMenu = () => {
  return (
    <div className="filter-menu">
      <FilterItem label="Species" icon={Search} hasSearch />
      <FilterItem label="Sequence Type" icon={Search} hasSearch />
      <FilterItem label="K Locus" icon={Search} hasSearch />
      <FilterItem label="Sample type" icon={Search} hasSearch />
      <FilterItem label="Resistance gene" icon={Search} hasSearch />
      <FilterItem label="Date" icon={Calendar} />
      <FilterItem label="Country" icon={MapPin} />
    </div>
  );
};

export default FilterMenu;
