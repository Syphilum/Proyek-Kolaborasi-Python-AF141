def main():
    tasks = []

    while True:
        print("\n===== To-Do List =====")
        print("1. Tambahkan Tugas")
        print("2. Tampilkan Tugas")
        print("3. Tandai Telah Selesai")
        print("4. Keluar")

        choice = input("Masukkan pilihan: ")

        if choice == '1':
            print()
            n_tasks = int(input("Berapa banyak tugas yang ingin anda tambahkan: "))
            
            for i in range(n_tasks):
                task = input("Masukkan Tugas: ")
                tasks.append({"task": task, "done": False})
                print("Tugas Ditambahkan!")

        elif choice == '2':
            print("\nDaftar Tugas:")
            for index, task in enumerate(tasks):
                status = "Selesai" if task["done"] else "Belum Selesai"
                print(f"{index + 1}. {task['task']} - {status}")

        elif choice == '3':
            task_index = int(input("Pilih Tugas Anda Yang Telah Selesai: ")) - 1
            if 0 <= task_index < len(tasks):
                tasks[task_index]["done"] = True
                print("Tugas Telah Selesai!")
            else:
                print("Nomor tugas tidak valid.")

        elif choice == '4':
            print("Keluar dari to-do list.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
#hello guys
