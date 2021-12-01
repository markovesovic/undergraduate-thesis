#include "precomp.hpp"

namespace cv 
{
    namespace gof 
    {
        void simulator::add_pattern(unsigned char* data, std::string pattern)
        {
            if (pattern == "glider")
            {
                this->add_glider(data);
            }
            else if (pattern == "oscilator")
            {
                this->add_oscilator(data);
            }
            else if (pattern == "gosper_gun")
            {
                this->add_gosper_glider_gun(data);
            }
            else if (pattern == "r_pentomino")
            {
                this->add_r_pentomino(data);
            }
            else if (pattern == "growth")
            {
                this->add_infinite_growth(data);
            }
        }


        void simulator::add_glider(unsigned char* data)
        {
            *(data + 2 * m_grid_size + 3) = 1;
            *(data + 3 * m_grid_size + 1) = 1;
            *(data + 3 * m_grid_size + 3) = 1;
            *(data + 4 * m_grid_size + 2) = 1;
            *(data + 4 * m_grid_size + 3) = 1;
        }

        void simulator::add_oscilator(unsigned char* data)
        {
            *(data + m_grid_size + 1) = 1;
            *(data + m_grid_size + 2) = 1;
            *(data + m_grid_size + 3) = 1;
        }

        void simulator::add_gosper_glider_gun(unsigned char* data)
        {

            int rows[] = {5, 5, 6, 6, 3, 3, 4, 4, 5, 5, 6, 6, 6, 6, 7, 7, 8, 8, 9, 9, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 3, 3, 4, 4};
            int cols[] = {1, 2, 1, 2, 13, 14, 12, 16, 11, 17, 11, 15, 17, 18, 11, 17, 12, 16, 13, 14, 25, 23, 25, 21, 22, 21, 22, 21, 22, 23, 25, 25, 35, 36, 35, 36};

            for(auto iter = 0; iter < 36; iter++)
            {
                *(data + rows[iter] * m_grid_size + cols[iter]) = 1;
            }
        }
        
        void simulator::add_infinite_growth(unsigned char* data)
        {
            int half = m_grid_size / 2;
            *(data + (1 + half) * m_grid_size + 7 + half) = 1;
            *(data + (2 + half) * m_grid_size + 5 + half) = 1;
            *(data + (2 + half) * m_grid_size + 7 + half) = 1;
            *(data + (2 + half) * m_grid_size + 8 + half) = 1;
            *(data + (3 + half) * m_grid_size + 5 + half) = 1;
            *(data + (3 + half) * m_grid_size + 7 + half) = 1;
            *(data + (4 + half) * m_grid_size + 5 + half) = 1;
            *(data + (5 + half) * m_grid_size + 3 + half) = 1;
            *(data + (6 + half) * m_grid_size + 1 + half) = 1;
            *(data + (6 + half) * m_grid_size + 3 + half) = 1;
            
        }
        void simulator::add_r_pentomino(unsigned char* data)
        {
            int half = m_grid_size / 2;
            *(data + half * m_grid_size + 2 + half) = 1;
            *(data + half * m_grid_size + 3 + half) = 1;
            *(data + (1 + half) * m_grid_size + 1 + half) = 1;
            *(data + (1 + half) * m_grid_size + 2 + half) = 1;
            *(data + (2 + half) * m_grid_size + 2 + half) = 1;
        }

    } // gof
} // cv