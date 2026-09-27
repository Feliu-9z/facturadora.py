import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime


def abrir_proforma():

    # =============================
    # VENTANA
    # =============================

    ventana = tk.Toplevel()
    ventana.title("Nueva Proforma")
    ventana.geometry("1000x750")
    # =============================
    # ÁREA DESPLAZABLE
    # =============================

    contenedor = ttk.Frame(ventana)

    contenedor.pack(
        fill="both",
        expand=True
    )


    canvas = tk.Canvas(
        contenedor,
        highlightthickness=0
    )


    scrollbar = ttk.Scrollbar(
        contenedor,
        orient="vertical",
        command=canvas.yview
    )


    canvas.configure(
        yscrollcommand=scrollbar.set
    )


    scrollbar.pack(
        side="right",
        fill="y"
    )


    canvas.pack(
        side="left",
        fill="both",
        expand=True
    )


    contenido = ttk.Frame(canvas)


    ventana_canvas = canvas.create_window(
        (0, 0),
        window=contenido,
        anchor="nw"
    )


    # =============================
    # ACTUALIZAR SCROLL
    # =============================

    def actualizar_scroll(event=None):

        canvas.configure(
            scrollregion=canvas.bbox("all")
        )


    contenido.bind(
        "<Configure>",
        actualizar_scroll
    )


    # =============================
    # AJUSTAR ANCHO
    # =============================

    def ajustar_ancho(event):

        canvas.itemconfigure(
            ventana_canvas,
            width=event.width
        )


    canvas.bind(
        "<Configure>",
        ajustar_ancho
    )


    # =============================
    # RUEDA DEL MOUSE
    # =============================

    def desplazar_mouse(event):

        canvas.yview_scroll(
            int(-1 * (event.delta / 120)),
            "units"
        )


    canvas.bind_all(
        "<MouseWheel>",
        desplazar_mouse
    )


    # Linux

    def desplazar_linux_arriba(event):

        canvas.yview_scroll(
            -1,
            "units"
        )


    def desplazar_linux_abajo(event):

        canvas.yview_scroll(
            1,
            "units"
        )


    canvas.bind_all(
        "<Button-4>",
        desplazar_linux_arriba
    )

    canvas.bind_all(
        "<Button-5>",
        desplazar_linux_abajo
    )




    # =============================
    # DATOS DE LA PROFORMA
    # =============================

    productos = []


    # =============================
    # TÍTULO
    # =============================

    titulo = ttk.Label(
        contenido,
        text="Nueva Proforma",
        font=("Arial", 20, "bold")
    )

    titulo.pack(pady=20)


    # =============================
    # DATOS GENERALES
    # =============================

    frame_cliente = ttk.LabelFrame(
        contenido,
        text="Datos generales",
        padding=15
    )

    frame_cliente.pack(
        fill="x",
        padx=30,
        pady=10
    )


    # Cliente

    ttk.Label(
        frame_cliente,
        text="Cliente:"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )

    entrada_cliente = ttk.Entry(
        frame_cliente,
        width=40
    )

    entrada_cliente.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )


    # País

    ttk.Label(
        frame_cliente,
        text="País:"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )

    entrada_pais = ttk.Entry(
        frame_cliente,
        width=40
    )

    entrada_pais.grid(
        row=1,
        column=1,
        padx=5,
        pady=5
    )


    # Fecha automática

    ttk.Label(
        frame_cliente,
        text="Fecha:"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )

    fecha_actual = datetime.now().strftime("%d/%m/%Y")

    ttk.Label(
        frame_cliente,
        text=fecha_actual
    ).grid(
        row=2,
        column=1,
        sticky="w",
        padx=5,
        pady=5
    )


    # =============================
    # REFERENCIAS
    # =============================

    frame_producto = ttk.LabelFrame(
        contenido,
        text="Agregar referencia",
        padding=15
    )

    frame_producto.pack(
        fill="x",
        padx=30,
        pady=10
    )


    # Referencia

    ttk.Label(
        frame_producto,
        text="Referencia:"
    ).grid(
        row=0,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )

    entrada_referencia = ttk.Entry(
        frame_producto,
        width=25
    )

    entrada_referencia.grid(
        row=0,
        column=1,
        padx=5,
        pady=5
    )


    # Precio

    ttk.Label(
        frame_producto,
        text="Precio unitario (USD):"
    ).grid(
        row=1,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )

    entrada_precio = ttk.Entry(
        frame_producto,
        width=15
    )

    entrada_precio.grid(
        row=1,
        column=1,
        sticky="w",
        padx=5,
        pady=5
    )


    # Cantidad

    ttk.Label(
        frame_producto,
        text="Cantidad:"
    ).grid(
        row=2,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )

    entrada_cantidad = ttk.Entry(
        frame_producto,
        width=15
    )

    entrada_cantidad.grid(
        row=2,
        column=1,
        sticky="w",
        padx=5,
        pady=5
    )


    # =============================
    # COLORES ADICIONALES
    # =============================

    tiene_colores = tk.StringVar(value="no")
    entradas_variantes = []
    cantidades_variantes = []
    widgets_cantidades = []
    cantidades_iguales = tk.StringVar(value="si")

    frame_variantes = ttk.Frame(
        frame_producto
    )

    frame_variantes.grid(
        row=4,
        column=0,
        columnspan=3,
        sticky="w",
        padx=5,
        pady=10
    )

    frame_variantes.grid_remove()


    def configurar_colores():

        # Limpiar variantes guardadas anteriormente
        entradas_variantes.clear()

        # Limpiar elementos visuales anteriores
        for widget in frame_variantes.winfo_children():
            widget.destroy()


        # Si el usuario selecciona NO, ocultar sección
        if tiene_colores.get() == "no":
            frame_variantes.grid_remove()
            return


        # Si selecciona SÍ, mostrar sección
        frame_variantes.grid()


        # Preguntar cantidad total de colores
        ttk.Label(
            frame_variantes,
            text="Cantidad total de colores (incluyendo el original):"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )


        entrada_num_colores = ttk.Entry(
            frame_variantes,
            width=10
        )

        entrada_num_colores.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )


        # ---------------------------------
        # CREAR CAMPOS PARA LOS COLORES
        # ---------------------------------

        def crear_campos_colores():

            # Eliminar campos anteriores,
            # pero conservar la primera fila
            for widget in frame_variantes.grid_slaves():

                fila = int(
                    widget.grid_info()["row"]
                )

                if fila > 0:
                    widget.destroy()


            # Limpiar datos anteriores
            entradas_variantes.clear()
            cantidades_variantes.clear()
            widgets_cantidades.clear()
            cantidades_iguales.set("si")


            # =============================
            # VALIDAR NÚMERO DE COLORES
            # =============================

            try:

                numero_colores = int(
                    entrada_num_colores.get()
                )

                if numero_colores < 2:
                    raise ValueError

            except ValueError:

                messagebox.showerror(
                    "Cantidad inválida",
                    "Si existen colores adicionales, "
                    "debe indicar al menos 2 colores en total."
                )

                return


            # =============================
            # COLOR ORIGINAL
            # =============================

            ttk.Label(
                frame_variantes,
                text="Color original: referencia sin modificación"
            ).grid(
                row=1,
                column=0,
                columnspan=2,
                sticky="w",
                padx=5,
                pady=5
            )


            # =============================
            # COLORES ADICIONALES
            # =============================

    tiene_colores = tk.StringVar(value="no")
    cantidades_iguales = tk.StringVar(value="si")

    entradas_variantes = []
    cantidades_variantes = []
    widgets_cantidades = []


    frame_variantes = ttk.Frame(
        frame_producto
    )

    frame_variantes.grid(
        row=4,
        column=0,
        columnspan=3,
        sticky="w",
        padx=5,
        pady=10
    )

    frame_variantes.grid_remove()


    # =============================
    # CONFIGURAR COLORES
    # =============================

    def configurar_colores():

        # Limpiar todo lo anterior
        for widget in frame_variantes.winfo_children():
            widget.destroy()

        entradas_variantes.clear()
        cantidades_variantes.clear()
        widgets_cantidades.clear()

        cantidades_iguales.set("si")


        # Si selecciona "No"
        if tiene_colores.get() == "no":
            frame_variantes.grid_remove()
            return


        # Si selecciona "Sí"
        frame_variantes.grid()


        ttk.Label(
            frame_variantes,
            text="Cantidad total de colores (incluyendo el original):"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5
        )


        entrada_num_colores = ttk.Entry(
            frame_variantes,
            width=10
        )

        entrada_num_colores.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )


        # =============================
        # CREAR CAMPOS DE COLORES
        # =============================

        def crear_campos_colores():

            # Borrar todo excepto la fila 0
            for widget in frame_variantes.grid_slaves():

                fila = int(
                    widget.grid_info()["row"]
                )

                if fila > 0:
                    widget.destroy()


            entradas_variantes.clear()
            cantidades_variantes.clear()
            widgets_cantidades.clear()

            cantidades_iguales.set("si")


            # Validar número de colores

            try:

                numero_colores = int(
                    entrada_num_colores.get()
                )

                if numero_colores < 2:
                    raise ValueError


            except ValueError:

                messagebox.showerror(
                    "Cantidad inválida",
                    "Debe indicar al menos 2 colores en total."
                )

                return


            # =============================
            # COLOR ORIGINAL
            # =============================

            ttk.Label(
                frame_variantes,
                text="Color original: referencia sin modificación"
            ).grid(
                row=1,
                column=0,
                columnspan=2,
                sticky="w",
                padx=5,
                pady=5
            )


            # =============================
            # COLORES ADICIONALES
            # =============================

            for i in range(1, numero_colores):

                ttk.Label(
                    frame_variantes,
                    text=f"Código del color adicional {i}:"
                ).grid(
                    row=i + 1,
                    column=0,
                    sticky="w",
                    padx=5,
                    pady=5
                )


                entrada_color = ttk.Entry(
                    frame_variantes,
                    width=10
                )

                entrada_color.grid(
                    row=i + 1,
                    column=1,
                    padx=5,
                    pady=5
                )


                entradas_variantes.append(
                    entrada_color
                )


            # =============================
            # PREGUNTA DE CANTIDADES
            # =============================

            fila_pregunta = numero_colores + 1


            ttk.Label(
                frame_variantes,
                text="¿Todos los colores tienen la misma cantidad?"
            ).grid(
                row=fila_pregunta,
                column=0,
                sticky="w",
                padx=5,
                pady=(15, 5)
            )


            frame_cantidades_opciones = ttk.Frame(
                frame_variantes
            )

            frame_cantidades_opciones.grid(
                row=fila_pregunta,
                column=1,
                sticky="w"
            )


            # =============================
            # CONFIGURAR CANTIDADES
            # =============================

            def configurar_cantidades():

                # Eliminar solamente los campos
                # dinámicos de cantidades

                for widget in widgets_cantidades:

                    if widget.winfo_exists():
                        widget.destroy()


                widgets_cantidades.clear()
                cantidades_variantes.clear()


                # Si son iguales no necesitamos
                # campos adicionales

                if cantidades_iguales.get() == "si":

                    entrada_cantidad.configure(
                        state="normal"
                    )

                    return


                entrada_cantidad.configure(
                    state="disabled"
                )


                # =========================
                # CANTIDAD ORIGINAL
                # =========================

                fila_actual = fila_pregunta + 1


                label_original = ttk.Label(
                    frame_variantes,
                    text="Cantidad del color original:"
                )

                label_original.grid(
                    row=fila_actual,
                    column=0,
                    sticky="w",
                    padx=5,
                    pady=5
                )


                entrada_original = ttk.Entry(
                    frame_variantes,
                    width=10
                )

                entrada_original.grid(
                    row=fila_actual,
                    column=1,
                    padx=5,
                    pady=5
                )


                widgets_cantidades.append(
                    label_original
                )

                widgets_cantidades.append(
                    entrada_original
                )

                cantidades_variantes.append(
                    entrada_original
                )


                # =========================
                # CANTIDADES DE COLORES
                # =========================

                for indice, entrada_color in enumerate(
                    entradas_variantes,
                    start=1
                ):

                    codigo = (
                        entrada_color
                        .get()
                        .strip()
                        .upper()
                    )


                    if not codigo:
                        codigo = f"Color {indice}"


                    fila_actual += 1


                    label_color = ttk.Label(
                        frame_variantes,
                        text=f"Cantidad de {codigo}:"
                    )

                    label_color.grid(
                        row=fila_actual,
                        column=0,
                        sticky="w",
                        padx=5,
                        pady=5
                    )


                    entrada_cantidad_color = ttk.Entry(
                        frame_variantes,
                        width=10
                    )

                    entrada_cantidad_color.grid(
                        row=fila_actual,
                        column=1,
                        padx=5,
                        pady=5
                    )


                    widgets_cantidades.append(
                        label_color
                    )

                    widgets_cantidades.append(
                        entrada_cantidad_color
                    )

                    cantidades_variantes.append(
                        entrada_cantidad_color
                    )


            # =============================
            # BOTONES SÍ / NO
            # =============================

            boton_cantidades_si = ttk.Radiobutton(
                frame_cantidades_opciones,
                text="Sí",
                variable=cantidades_iguales,
                value="si",
                command=configurar_cantidades
            )

            boton_cantidades_si.pack(
                side="left",
                padx=5
            )


            boton_cantidades_no = ttk.Radiobutton(
                frame_cantidades_opciones,
                text="No",
                variable=cantidades_iguales,
                value="no",
                command=configurar_cantidades
            )

            boton_cantidades_no.pack(
                side="left",
                padx=5
            )


        # =============================
        # BOTÓN CONFIGURAR COLORES
        # =============================

        boton_configurar_colores = ttk.Button(
            frame_variantes,
            text="Configurar colores",
            command=crear_campos_colores
        )

        boton_configurar_colores.grid(
            row=0,
            column=2,
            padx=10,
            pady=5
        )

    # Pregunta de colores

    ttk.Label(
        frame_producto,
        text="¿Tiene colores adicionales?"
    ).grid(
        row=3,
        column=0,
        sticky="w",
        padx=5,
        pady=5
    )


    frame_colores_opciones = ttk.Frame(
        frame_producto
    )

    frame_colores_opciones.grid(
        row=3,
        column=1,
        sticky="w"
    )


    ttk.Radiobutton(
        frame_colores_opciones,
        text="No",
        variable=tiene_colores,
        value="no",
        command=configurar_colores
    ).pack(
        side="left",
        padx=5
    )


    ttk.Radiobutton(
        frame_colores_opciones,
        text="Sí",
        variable=tiene_colores,
        value="si",
        command=configurar_colores
    ).pack(
        side="left",
        padx=5
    )


    # =============================
    # TABLA
    # =============================

    frame_tabla = ttk.LabelFrame(
        contenido,
        text="Referencias agregadas",
        padding=10
    )

    frame_tabla.pack(
        fill="both",
        expand=True,
        padx=30,
        pady=10
    )


    columnas = (
        "referencia",
        "cantidad",
        "precio",
        "subtotal"
    )


    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings"
    )


    tabla.heading(
        "referencia",
        text="Referencia"
    )

    tabla.heading(
        "cantidad",
        text="Cantidad"
    )

    tabla.heading(
        "precio",
        text="Precio Unitario"
    )

    tabla.heading(
        "subtotal",
        text="Subtotal"
    )


    tabla.pack(
        fill="both",
        expand=True
    )
        # =============================
    # TOTALES DE LA TABLA
    # =============================

    # =============================
    # TOTALES DE LA TABLA
    # =============================

    frame_totales = ttk.Frame(
        frame_tabla
    )

    frame_totales.pack(
        fill="x",
        pady=10
    )


    texto_cantidad_total = tk.StringVar(
        value="Cantidad total: 0"
    )

    texto_subtotal_general = tk.StringVar(
        value="Subtotal: $0.00"
    )


    ttk.Label(
        frame_totales,
        textvariable=texto_cantidad_total,
        font=("Arial", 11, "bold")
    ).pack(
        side="left",
        padx=20
    )


    ttk.Label(
        frame_totales,
        textvariable=texto_subtotal_general,
        font=("Arial", 11, "bold")
    ).pack(
        side="right",
        padx=20
    )


    # =============================
    # BOTONES DE GESTIÓN
    # =============================

    frame_botones_tabla = ttk.Frame(
        frame_tabla
    )

    frame_botones_tabla.pack(
        pady=10
    )


    # =============================
    # RECALCULAR TOTALES
    # =============================

    def actualizar_totales():

        cantidad_total = sum(
            producto["cantidad"]
            for producto in productos
        )

        subtotal_general = sum(
            producto["subtotal"]
            for producto in productos
        )

        texto_cantidad_total.set(
            f"Cantidad total: {cantidad_total}"
        )

        texto_subtotal_general.set(
            f"Subtotal: ${subtotal_general:,.2f}"
        )


    # =============================
    # ELIMINAR REFERENCIA
    # =============================

    def eliminar_referencia():

        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Sin selección",
                "Seleccione una referencia de la tabla."
            )

            return


        item = seleccion[0]

        valores = tabla.item(
            item,
            "values"
        )

        referencia = valores[0]


        confirmar = messagebox.askyesno(
            "Eliminar referencia",
            f"¿Desea eliminar {referencia}?"
        )


        if not confirmar:
            return


        for producto in productos:

            if producto["referencia"] == referencia:

                productos.remove(
                    producto
                )

                break


        tabla.delete(
            item
        )


        actualizar_totales()


    # =============================
    # EDITAR REFERENCIA
    # =============================

    def editar_referencia():

        seleccion = tabla.selection()

        if not seleccion:

            messagebox.showwarning(
                "Sin selección",
                "Seleccione una referencia de la tabla."
            )

            return


        item = seleccion[0]

        valores = tabla.item(
            item,
            "values"
        )

        referencia_actual = valores[0]


        producto_actual = None


        for producto in productos:

            if producto["referencia"] == referencia_actual:

                producto_actual = producto
                break


        if producto_actual is None:
            return


        # =============================
        # VENTANA DE EDICIÓN
        # =============================

        ventana_editar = tk.Toplevel(
            ventana
        )

        ventana_editar.title(
            "Editar referencia"
        )

        ventana_editar.geometry(
            "420x300"
        )


        ttk.Label(
            ventana_editar,
            text="Editar referencia",
            font=("Arial", 16, "bold")
        ).pack(
            pady=15
        )


        frame_editar = ttk.Frame(
            ventana_editar
        )

        frame_editar.pack(
            padx=20,
            pady=10
        )


        # Referencia

        ttk.Label(
            frame_editar,
            text="Referencia:"
        ).grid(
            row=0,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )


        entrada_editar_referencia = ttk.Entry(
            frame_editar,
            width=20
        )

        entrada_editar_referencia.grid(
            row=0,
            column=1,
            padx=5,
            pady=5
        )

        entrada_editar_referencia.insert(
            0,
            producto_actual["referencia"]
        )


        # Cantidad

        ttk.Label(
            frame_editar,
            text="Cantidad:"
        ).grid(
            row=1,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )


        entrada_editar_cantidad = ttk.Entry(
            frame_editar,
            width=20
        )

        entrada_editar_cantidad.grid(
            row=1,
            column=1,
            padx=5,
            pady=5
        )

        entrada_editar_cantidad.insert(
            0,
            str(producto_actual["cantidad"])
        )


        # Precio

        ttk.Label(
            frame_editar,
            text="Precio unitario:"
        ).grid(
            row=2,
            column=0,
            padx=5,
            pady=5,
            sticky="w"
        )


        entrada_editar_precio = ttk.Entry(
            frame_editar,
            width=20
        )

        entrada_editar_precio.grid(
            row=2,
            column=1,
            padx=5,
            pady=5
        )

        entrada_editar_precio.insert(
            0,
            str(producto_actual["precio"])
        )


        # =============================
        # GUARDAR CAMBIOS
        # =============================

        def guardar_cambios():

            nueva_referencia = (
                entrada_editar_referencia
                .get()
                .strip()
                .upper()
            )


            if not nueva_referencia:

                messagebox.showerror(
                    "Error",
                    "La referencia no puede estar vacía."
                )

                return


            try:

                nueva_cantidad = int(
                    entrada_editar_cantidad
                    .get()
                    .strip()
                )

                if nueva_cantidad <= 0:
                    raise ValueError


            except ValueError:

                messagebox.showerror(
                    "Error",
                    "La cantidad debe ser un entero mayor que 0."
                )

                return


            try:

                nuevo_precio = float(
                    entrada_editar_precio
                    .get()
                    .strip()
                )

                if nuevo_precio <= 0:
                    raise ValueError


            except ValueError:

                messagebox.showerror(
                    "Error",
                    "El precio debe ser mayor que 0."
                )

                return


            # Evitar referencia duplicada

            for producto in productos:

                if (
                    producto is not producto_actual
                    and producto["referencia"] == nueva_referencia
                ):

                    messagebox.showerror(
                        "Referencia duplicada",
                        f"La referencia {nueva_referencia} ya existe."
                    )

                    return


            nuevo_subtotal = (
                nueva_cantidad
                * nuevo_precio
            )


            # Actualizar datos internos

            producto_actual["referencia"] = nueva_referencia
            producto_actual["cantidad"] = nueva_cantidad
            producto_actual["precio"] = nuevo_precio
            producto_actual["subtotal"] = nuevo_subtotal


            # Actualizar tabla

            tabla.item(
                item,
                values=(
                    nueva_referencia,
                    nueva_cantidad,
                    f"${nuevo_precio:.2f}",
                    f"${nuevo_subtotal:.2f}"
                )
            )


            actualizar_totales()

            ventana_editar.destroy()


        ttk.Button(
            ventana_editar,
            text="Guardar cambios",
            command=guardar_cambios
        ).pack(
            pady=15
        )


    # =============================
    # BOTONES EDITAR / ELIMINAR
    # =============================

    ttk.Button(
        frame_botones_tabla,
        text="Editar seleccionada",
        command=editar_referencia
    ).pack(
        side="left",
        padx=10
    )


    ttk.Button(
        frame_botones_tabla,
        text="Eliminar seleccionada",
        command=eliminar_referencia
    ).pack(
        side="left",
        padx=10
    )

    # =============================
    # FUNCIÓN AGREGAR
    # =============================

    def agregar_referencia():

        referencia = entrada_referencia.get().strip().upper()
        cantidad_texto = entrada_cantidad.get().strip()
        precio_texto = entrada_precio.get().strip()


        # Validar referencia

        if not referencia:

            messagebox.showerror(
                "Error",
                "Debe ingresar una referencia."
            )

            return


        # Validar cantidad

        # =============================
        # VALIDAR CANTIDAD GENERAL
        # =============================

        cantidad = None


        # Solo necesitamos la cantidad general
        # cuando no hay colores o las cantidades son iguales
        if (
            tiene_colores.get() == "no"
            or cantidades_iguales.get() == "si"
        ):

            try:

                cantidad = int(
                    entrada_cantidad.get().strip()
                )

                if cantidad <= 0:
                    raise ValueError


            except ValueError:

                messagebox.showerror(
                    "Error",
                    "La cantidad debe ser un número entero mayor que 0."
                )

                return


        # Validar precio

        try:

            precio = float(precio_texto)

            if precio <= 0:
                raise ValueError

        except ValueError:

            messagebox.showerror(
                "Error",
                "El precio debe ser un número mayor que 0."
            )

            return


        # =============================
        # PREPARAR REFERENCIAS
        # =============================

        referencias_a_agregar = [referencia]
                # =============================
        # EVITAR REFERENCIAS DUPLICADAS
        # =============================

        referencias_existentes = {
            producto["referencia"]
            for producto in productos
        }


        for referencia_nueva in referencias_a_agregar:

            if referencia_nueva in referencias_existentes:

                messagebox.showerror(
                    "Referencia duplicada",
                    f"La referencia {referencia_nueva} "
                    "ya fue agregada."
                )

                return


        # Si existen colores adicionales
        if tiene_colores.get() == "si":

            # Comprobar que se configuraron
            if not entradas_variantes:

                messagebox.showerror(
                    "Colores sin configurar",
                    "Debe configurar los colores adicionales "
                    "antes de agregar la referencia."
                )

                return


            # Leer cada código de color
            for entrada_color in entradas_variantes:

                codigo_color = (
                    entrada_color
                    .get()
                    .strip()
                    .upper()
                )


                # No permitir códigos vacíos
                if not codigo_color:

                    messagebox.showerror(
                        "Color incompleto",
                        "Debe ingresar el código de todos "
                        "los colores adicionales."
                    )

                    return


                # Construir referencia final
                referencia_color = (
                    f"{referencia}({codigo_color})"
                )


                referencias_a_agregar.append(
                    referencia_color
                )


        # =============================
        # AGREGAR PRODUCTOS
        # =============================

        # =============================
        # DETERMINAR CANTIDADES
        # =============================

        cantidades_a_agregar = []


        # Caso 1:
        # No hay colores o todas las cantidades son iguales
        if (
            tiene_colores.get() == "no"
            or cantidades_iguales.get() == "si"
        ):

            cantidades_a_agregar = [
                cantidad
            ] * len(referencias_a_agregar)


        # Caso 2:
        # Cada color tiene una cantidad diferente
        else:

            # Debe existir una cantidad por cada referencia
            if len(cantidades_variantes) != len(
                referencias_a_agregar
            ):

                messagebox.showerror(
                    "Cantidades incompletas",
                    "Debe indicar la cantidad de cada variante."
                )

                return


            # Leer cantidades individuales
            for entrada in cantidades_variantes:

                try:

                    cantidad_variante = int(
                        entrada.get().strip()
                    )

                    if cantidad_variante <= 0:
                        raise ValueError


                except ValueError:

                    messagebox.showerror(
                        "Cantidad inválida",
                        "Todas las cantidades deben ser "
                        "números enteros mayores que 0."
                    )

                    return


                cantidades_a_agregar.append(
                    cantidad_variante
                )


        # =============================
        # AGREGAR PRODUCTOS
        # =============================

        for referencia_final, cantidad_final in zip(
            referencias_a_agregar,
            cantidades_a_agregar
        ):

            subtotal = (
                cantidad_final
                * precio
            )


            producto = {
                "referencia": referencia_final,
                "cantidad": cantidad_final,
                "precio": precio,
                "subtotal": subtotal
            }


            productos.append(
                producto
            )


            tabla.insert(
                "",
                "end",
                values=(
                    referencia_final,
                    cantidad_final,
                    f"${precio:.2f}",
                    f"${subtotal:.2f}"
                )
            )


        actualizar_totales()


        # Limpiar campos

        # Limpiar campos

        entrada_referencia.delete(0, tk.END)
        
        entrada_cantidad.configure(
            state="normal"
        )
        entrada_cantidad.delete(0, tk.END)

        entrada_precio.delete(0, tk.END)


        # Restablecer colores

        tiene_colores.set("no")
        configurar_colores()


        # Devolver cursor a referencia

        entrada_referencia.focus()


    # =============================
    # BOTÓN AGREGAR
    # =============================

    boton_agregar = ttk.Button(
        frame_producto,
        text="Agregar referencia",
        command=agregar_referencia
    )

    boton_agregar.grid(
        row=5,
        column=0,
        columnspan=2,
        pady=15
    )