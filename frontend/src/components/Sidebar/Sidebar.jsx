import { useState } from "react";
import { Search, Calendar, MapPin, ChevronDown } from "lucide-react";
import "./Sidebar.css";

const FilterItem = ({
  label,
  icon: Icon,
  hasSearch = false,
  dados,
  campo,
  selectedOptions,
  onToggleOption,
}) => {
  const [open, setOpen] = useState(false);
  const [searchValue, setSearchValue] = useState("");

  const options = Array.from(
    new Set(dados.map((item) => item[campo]).filter(Boolean))
  );

  const filteredOptions = options.filter((opt) =>
    opt.toLowerCase().includes(searchValue.toLowerCase())
  );

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
          <ul className="filter-options">
            {filteredOptions.map((option, idx) => (
              <li
                key={idx}
                className={`filter-option ${
                  selectedOptions.includes(option) ? "selected" : ""
                }`}
                onClick={() => onToggleOption(campo, option)}
              >
                {option}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
};

const Sidebar = ({ dados, onApplyFilters, onClearFilters }) => {
  const [selectedFilters, setSelectedFilters] = useState({});

  const handleToggleOption = (campo, option) => {
    setSelectedFilters((prev) => {
      const current = prev[campo] || [];
      return {
        ...prev,
        [campo]: current.includes(option)
          ? current.filter((o) => o !== option)
          : [...current, option],
      };
    });
  };

  const handleClearFilters = () => {
    setSelectedFilters({});
    onClearFilters(); // Chama a função de limpar filtros
  };

  const handleApplyFilters = () => {
    onApplyFilters(selectedFilters); // Passa os filtros aplicados para o Home
  };

  const filtros = [
    { label: "Species", icon: Search, campo: "Organism", hasSearch: true },
    { label: "Sequence Type", icon: Search, campo: "Sequencing platform_1", hasSearch: true },
    { label: "K Locus", icon: Search, campo: "Kapsule Locus", hasSearch: true },
    { label: "Sample type", icon: Search, campo: "Type of sample", hasSearch: true },
    { label: "Resistance gene", icon: Search, campo: "Carbapenem resistance", hasSearch: true },
    { label: "Date", icon: Calendar, campo: "Collection date" },
    { label: "Country", icon: MapPin, campo: "Country" },
  ];

  return (
    <div className="side-menu">
      {filtros.map((f) => (
        <FilterItem
          key={f.campo}
          label={f.label}
          icon={f.icon}
          dados={dados}
          campo={f.campo}
          hasSearch={f.hasSearch}
          selectedOptions={selectedFilters[f.campo] || []}
          onToggleOption={handleToggleOption}
        />
      ))}

      <div className="filter-buttons">
        <button className="apply-btn" onClick={handleApplyFilters}>Aplicar Filtros</button>
        <button className="clear-btn" onClick={handleClearFilters}>Limpar Filtros</button>
      </div>
    </div>
  );
};

export default Sidebar;
