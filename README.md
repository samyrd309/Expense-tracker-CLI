# Expense Tracker CLI

Una aplicación de línea de comandos para gestionar tus finanzas de manera sencilla. Permite agregar, eliminar, y ver tus gastos, además de proporcionar un resumen de los mismos.

## Requisitos

La aplicación debe cumplir con las siguientes características:

- Los usuarios pueden **agregar un gasto** con una descripción y un monto.
- Los usuarios pueden **actualizar un gasto** existente.
- Los usuarios pueden **eliminar un gasto**.
- Los usuarios pueden **ver todos los gastos** registrados.
- Los usuarios pueden **ver un resumen de todos los gastos**.
- Los usuarios pueden **ver un resumen de los gastos de un mes específico** (del año actual).

### Funcionalidades adicionales sugeridas:

- **Categorías de gastos**: Permitir a los usuarios filtrar gastos por categoría.
- **Presupuesto mensual**: Permitir a los usuarios establecer un presupuesto mensual y mostrar una advertencia si se excede.
- **Exportar a CSV**: Permitir a los usuarios exportar los gastos a un archivo CSV.

---

## Comandos y ejemplos

### Agregar un gasto
Agrega un nuevo gasto proporcionando una descripción y un monto:
```bash
python main.py add --description "Lunch" --amount 20
# Expense added successfully (ID: 1) 
```

### Listar todos los gastos
Muestra todos los gastos registrados:
```bash
python main.py list
# ID  Date       Description  Amount
# 1   2025-04-12  Lunch        $20
# 2   2025-04-12  Dinner       $10
```


### Mostrar el resumen de gastos
Muestra el total de todos los gastos registrados:
```bash
python main.py summary
# Total expenses: $30
```


### Eliminar un gasto
Elimina un gasto específico utilizando su ID:
```bash
python main.py delete --id 1
# Expense deleted successfully
```